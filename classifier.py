"""
classifier.py — Puente
Single-purpose AI classifier. Takes a patient's free-text message and returns
one of the 8 resource category codes, or None if the message cannot be
confidently classified.

This is the only AI component in the system. It does not generate any
patient-facing text — it only returns a category code that the existing
routing logic uses exactly as it would a numbered menu choice.
"""

import os
from pathlib import Path
import anthropic
from dotenv import dotenv_values as _dotenv_values


def _get_api_key() -> str:
    key = os.getenv("ANTHROPIC_API_KEY", "")
    if not key:
        # Shell may export the var as empty; read the .env file directly
        # so we don't disturb other env vars (e.g. PORT set on the command line).
        key = _dotenv_values(Path(__file__).parent / ".env").get("ANTHROPIC_API_KEY", "")
    return key

VALID_CATEGORIES = {
    "general",
    "dental",
    "vision",
    "medications",
    "mental_health",
    "cancer",
    "womens",
    "all",
}

SYSTEM_PROMPT = """You are a medical triage assistant that reads a patient's
message and classifies it into exactly one health resource category.

You must respond with ONLY one of these exact category codes — nothing else,
no punctuation, no explanation:

  general       — doctor visits, checkups, general illness, vaccines, any care
                  that does not fit another category
  dental        — teeth, gums, toothache, dental pain, dentist
  vision        — eyes, glasses, eyesight, optometrist, contact lenses
  medications   — prescriptions, specific drugs, can't afford medicine, pharmacy
  mental_health — anxiety, depression, stress, therapy, counseling, substance use,
                  emotional health, suicide risk, psychiatric care
  cancer        — cancer screenings, mammograms, colonoscopy, cervical screening
  womens        — pregnancy, prenatal care, birth control, gynecology, women's
                  reproductive health
  all           — patient wants to see everything, not sure what they need,
                  or their message is too vague to classify confidently

Rules:
- Respond with ONLY the category code. No other words.
- If the message is in Spanish, Farsi, Hindi, or any other language, still return the English category code.
- If genuinely unsure between two categories, pick the broader one (general
  beats a specific category when uncertain).
- If the message is completely unrelated to health (e.g. spam, random letters),
  return: all
- Never return anything other than one of the eight codes above."""


def classify_message(patient_text):
    """
    Sends the patient's message to the Claude API and returns a category code.

    Returns one of the VALID_CATEGORIES strings, or None if:
    - The API call fails for any reason
    - The API returns something unexpected
    - The ANTHROPIC_API_KEY environment variable is not set

    Failure always returns None — the caller handles the fallback.
    """
    api_key = _get_api_key()
    if not api_key:
        return None

    try:
        client = anthropic.Anthropic(api_key=api_key)

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=10,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": patient_text}
            ],
        )

        raw = message.content[0].text.strip().lower()

        if raw in VALID_CATEGORIES:
            return raw

        return None

    except Exception:
        # Any API error (network, auth, rate limit) returns None gracefully.
        # The caller will show the patient a friendly fallback message.
        return None
