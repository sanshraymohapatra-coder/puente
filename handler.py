"""
handler.py — Puente
Core message routing logic. Receives a raw SMS body + phone number,
returns the text response to send back.

Session steps:
  menu           → waiting for the user to pick a category (1-8)
  awaiting_zip   → waiting for the user's zip code
  results        → showing results, waiting for MORE or START
"""

import re
from database import (
    make_session_key, get_session, save_session,
    delete_session, get_resources, log_analytic,
)
from strings import (
    s, detect_language, format_resource,
    MENU_CHOICES, STOP_WORDS, HELP_WORDS,
    START_WORDS, MORE_WORDS, EN_WORDS, ES_WORDS,
    FA_WORDS, HI_WORDS,
)
from classifier import classify_message


def is_valid_zip(text: str) -> bool:
    return bool(re.match(r"^\d{5}$", text.strip()))


def handle_message(body: str, phone_number: str) -> str:
    """
    Main entry point. Takes the raw SMS body and the sender's phone number,
    returns the string to SMS back to them.
    """
    msg = body.strip()
    msg_upper = msg.upper()
    session_key = make_session_key(phone_number)

    # ── Global keywords — handled before any session logic ──────────────────

    if msg_upper in STOP_WORDS:
        existing = get_session(session_key)
        delete_session(session_key)
        if msg_upper in {"ALTO", "CANCELAR"}:
            lang = "es"
        else:
            lang = existing["language"] if existing else "en"
        return s(lang, "stop")

    if msg_upper in HELP_WORDS:
        session = get_session(session_key)
        lang = "es" if msg_upper == "AYUDA" else (session["language"] if session else "en")
        return s(lang, "help")

    if msg_upper in EN_WORDS:
        save_session(session_key, "menu", language="en")
        return s("en", "welcome")

    if msg_upper in ES_WORDS:
        save_session(session_key, "menu", language="es")
        return s("es", "welcome")

    if msg_upper in FA_WORDS or msg in FA_WORDS:
        save_session(session_key, "menu", language="fa")
        return s("fa", "welcome")

    if msg_upper in HI_WORDS or msg in HI_WORDS:
        save_session(session_key, "menu", language="hi")
        return s("hi", "welcome")

    # ── Load session ──────────────────────────────────────────────────────────

    session = get_session(session_key)

    # Determine language
    if session:
        lang = session.get("language", "en")
    else:
        lang = detect_language(msg)

    # ── No session or START → show menu ──────────────────────────────────────

    if not session or msg_upper in START_WORDS:
        prefix = s(lang, "start_prefix") if session else ""
        save_session(session_key, "menu", language=lang)
        return prefix + s(lang, "welcome")

    step = session.get("step", "menu")

    # ── Step: menu ────────────────────────────────────────────────────────────

    if step == "menu":
        choice = MENU_CHOICES.get(msg.strip())
        if choice:
            save_session(session_key, "awaiting_zip", category=choice, language=lang)
            return s(lang, "ask_zip")

        detected = classify_message(msg)
        if detected:
            category_label = s(lang, f"cat_{detected}")
            save_session(session_key, "awaiting_zip", category=detected, language=lang)
            return s(lang, "freetext_match", category=category_label)

        return s(lang, "freetext_nomatch")

    # ── Step: awaiting_zip ────────────────────────────────────────────────────

    if step == "awaiting_zip":
        if not is_valid_zip(msg):
            return s(lang, "invalid_zip")

        zip_code = msg.strip()
        category = session.get("category", "general")

        # Log aggregate analytic (no personal data)
        log_analytic(category, zip_code)

        results, has_more = get_resources(category, zip_code, offset=0, limit=3)

        if not results:
            return s(lang, "no_results")

        # Save state for MORE
        save_session(session_key, "results", category=category,
                     language=lang, zip_code=zip_code, offset=3)

        return _build_results_message(results, has_more, zip_code, lang)

    # ── Step: results ─────────────────────────────────────────────────────────

    if step == "results":
        if msg_upper in MORE_WORDS:
            category = session.get("category", "general")
            zip_code  = session.get("zip_code", "")
            offset    = session.get("last_offset", 3)

            results, has_more = get_resources(category, zip_code, offset=offset, limit=3)

            if not results:
                save_session(session_key, "menu", language=lang)
                return s(lang, "no_results") + "\n" + s(lang, "no_more")

            new_offset = offset + len(results)
            save_session(session_key, "results", category=category,
                         language=lang, zip_code=zip_code, offset=new_offset)

            return _build_results_message(results, has_more, zip_code, lang)

        # If they send a digit, start a new search
        choice = MENU_CHOICES.get(msg.strip())
        if choice:
            save_session(session_key, "awaiting_zip", category=choice, language=lang)
            return s(lang, "ask_zip")

        # Any other message: try free-text category detection first
        detected = classify_message(msg)
        if detected:
            category_label = s(lang, f"cat_{detected}")
            save_session(session_key, "awaiting_zip", category=detected, language=lang)
            return s(lang, "freetext_match", category=category_label)

        # No match — reset to menu
        save_session(session_key, "menu", language=lang)
        return s(lang, "no_more") + "\n\n" + s(lang, "welcome")

    # ── Fallback ──────────────────────────────────────────────────────────────

    save_session(session_key, "menu", language=lang)
    return s(lang, "welcome")


def _build_results_message(results: list, has_more: bool,
                            zip_code: str, lang: str) -> str:
    """Format a list of resources into a single SMS-friendly string."""
    header = s(lang, "results_header", count=len(results), zip=zip_code)
    blocks = []
    for i, r in enumerate(results, 1):
        blocks.append(f"{i}. {format_resource(r, lang)}")
    footer = s(lang, "more_prompt") if has_more else s(lang, "no_more")
    return header + "\n".join(blocks) + "\n" + footer
