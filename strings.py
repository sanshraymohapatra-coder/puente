"""
strings.py — Puente
All user-facing text in English (en) and Spanish (es).
To add a new language, duplicate one of the language blocks and translate.
"""

# ── All response strings ──────────────────────────────────────────────────────

STRINGS = {
    "en": {
        "welcome": (
            "Hi! I'm Puente \u2014 I'll help you find free health resources nearby.\n\n"
            "What do you need?\n\n"
            "1 \u2013 General care\n"
            "2 \u2013 Dental\n"
            "3 \u2013 Vision\n"
            "4 \u2013 Medications\n"
            "5 \u2013 Mental health\n"
            "6 \u2013 Cancer screenings\n"
            "7 \u2013 Women's health\n"
            "8 \u2013 All resources\n\n"
            "Para Espanol, responde ES."
        ),
        "ask_zip": (
            "Got it. What's your zip code?\n\n"
            "(We use this only to find nearby resources \u2014 we never save it.)"
        ),
        "results_header": "Here are {count} free options near {zip}:\n",
        "walk_in": "Walk-ins welcome",
        "more_prompt": "\nReply MORE for more results, or START to search again.",
        "no_more": "\nReply START to search again.",
        "no_results": (
            "We don't have resources listed for that area yet.\n\n"
            "Try a nearby zip code or reply START to search again."
        ),
        "invalid_zip": (
            "That doesn't look like a valid zip code.\n\n"
            "Please reply with your 5-digit zip code (e.g. 85034)."
        ),
        "invalid_choice": "Please reply with a number 1\u20138 to choose a category.",
        "freetext_nomatch": (
            "I wasn't sure how to help with that. Try replying with a number:\n\n"
            "1 - Doctor visit or general care\n"
            "2 - Dental (teeth)\n"
            "3 - Vision (eyes)\n"
            "4 - Medications\n"
            "5 - Mental health\n"
            "6 - Cancer screenings\n"
            "7 - Women's health\n"
            "8 - Show me everything"
        ),
        "freetext_match": (
            "It sounds like you need {category}.\n\n"
            "What's your zip code? (We use this only to find nearby resources "
            "\u2014 we never save it.)"
        ),
        "cat_general":      "general health care",
        "cat_dental":       "dental care",
        "cat_vision":       "vision care",
        "cat_medications":  "help with medications",
        "cat_mental_health": "mental health support",
        "cat_cancer":       "cancer screenings",
        "cat_womens":       "women's health care",
        "cat_all":          "health resources",
        "help": (
            "Puente helps you find free health resources by text message.\n\n"
            "Reply START to begin a new search.\n"
            "Reply STOP to stop receiving messages."
        ),
        "stop": "You've been unsubscribed. Text us any time to search for resources again.",
        "start_prefix": "Welcome back! ",
        "event_prefix": "EVENT ",
        "hours_prefix": "Hours: ",
        "phone_prefix": "Call: ",
        "walkin_label": "No appointment needed — just show up",
        "notes_prefix": "",
    },
    "es": {
        "welcome": (
            "Hola! Soy Puente \u2014 te ayudo a encontrar recursos de salud gratuitos.\n\n"
            "Que necesitas?\n\n"
            "1 \u2013 Atencion general\n"
            "2 \u2013 Dental\n"
            "3 \u2013 Vision\n"
            "4 \u2013 Medicamentos\n"
            "5 \u2013 Salud mental\n"
            "6 \u2013 Examenes de cancer\n"
            "7 \u2013 Salud de la mujer\n"
            "8 \u2013 Todos los recursos\n\n"
            "For English, reply EN."
        ),
        "ask_zip": (
            "Entendido. Cual es tu codigo postal?\n\n"
            "(Solo lo usamos para encontrar recursos cercanos \u2014 nunca lo guardamos.)"
        ),
        "results_header": "Aqui hay {count} opciones gratuitas cerca de {zip}:\n",
        "walk_in": "Sin cita necesaria",
        "more_prompt": "\nResponde MAS para mas resultados, o INICIO para buscar de nuevo.",
        "no_more": "\nResponde INICIO para buscar de nuevo.",
        "no_results": (
            "Aun no tenemos recursos en esa area.\n\n"
            "Intenta un codigo postal cercano o responde INICIO para buscar de nuevo."
        ),
        "invalid_zip": (
            "Eso no parece un codigo postal valido.\n\n"
            "Por favor responde con tu codigo postal de 5 digitos (ej. 85034)."
        ),
        "invalid_choice": "Por favor responde con un numero del 1 al 8 para elegir una categoria.",
        "freetext_nomatch": (
            "No estoy seguro de como ayudarte con eso. Intenta responder con un numero:\n\n"
            "1 - Doctor o atencion general\n"
            "2 - Dental (dientes)\n"
            "3 - Vision (ojos)\n"
            "4 - Medicamentos\n"
            "5 - Salud mental\n"
            "6 - Examenes de cancer\n"
            "7 - Salud de la mujer\n"
            "8 - Ver todo"
        ),
        "freetext_match": (
            "Parece que necesitas {category}.\n\n"
            "Cual es tu codigo postal? (Solo lo usamos para encontrar recursos "
            "cercanos — nunca lo guardamos.)"
        ),
        "cat_general":      "atencion medica general",
        "cat_dental":       "atencion dental",
        "cat_vision":       "atencion de la vista",
        "cat_medications":  "ayuda con medicamentos",
        "cat_mental_health": "apoyo de salud mental",
        "cat_cancer":       "examenes de cancer",
        "cat_womens":       "salud de la mujer",
        "cat_all":          "recursos de salud",
        "help": (
            "Puente te ayuda a encontrar recursos de salud gratuitos por mensaje de texto.\n\n"
            "Responde INICIO para comenzar una nueva busqueda.\n"
            "Responde ALTO para dejar de recibir mensajes."
        ),
        "stop": "Has cancelado la suscripcion. Escribenos cuando quieras buscar recursos de nuevo.",
        "start_prefix": "Bienvenido de nuevo! ",
        "event_prefix": "EVENTO ",
        "hours_prefix": "Horario: ",
        "phone_prefix": "Llama: ",
        "walkin_label": "No necesitas cita — solo llega",
        "notes_prefix": "",
    },
}

# Maps the digit a user texts to a DB category name
MENU_CHOICES = {
    "1": "general",
    "2": "dental",
    "3": "vision",
    "4": "medications",
    "5": "mental_health",
    "6": "cancer",
    "7": "womens",
    "8": "all",
}

# Keywords that trigger specific behaviors
STOP_WORDS  = {"STOP", "ALTO", "CANCEL", "CANCELAR", "UNSUBSCRIBE"}
HELP_WORDS  = {"HELP", "AYUDA", "INFO"}
START_WORDS = {"START", "INICIO", "BEGIN", "HI", "HELLO", "HOLA"}
MORE_WORDS  = {"MORE", "MAS", "MÁS", "SIGUIENTE", "NEXT"}
EN_WORDS    = {"EN", "ENGLISH"}
ES_WORDS    = {"ES", "ESPANOL", "ESPAÑOL"}


# ── Helpers ───────────────────────────────────────────────────────────────────

def s(lang: str, key: str, **kwargs) -> str:
    """Get a string in the given language, with optional format substitution."""
    text = STRINGS.get(lang, STRINGS["en"]).get(key, "")
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, ValueError):
            pass
    return text


def detect_language(text: str) -> str:
    """
    Simple language detection from the first message.
    Defaults to English when ambiguous.
    """
    t = text.lower().strip()

    if t in {"es", "español", "espanol", "hola", "ayuda", "inicio", "alto", "mas"}:
        return "es"
    if t in {"en", "english", "hi", "hello", "help", "start", "stop", "more"}:
        return "en"

    # Count Spanish indicator words
    spanish_markers = {
        "que", "por", "para", "gracias", "como", "donde",
        "salud", "medico", "clinica", "clínica", "necesito",
        "tengo", "busco", "gratis", "ayuda", "favor",
    }
    words = set(t.split())
    if len(words & spanish_markers) >= 1:
        return "es"

    return "en"


def format_resource(resource: dict, lang: str) -> str:
    """
    Format a single resource record into a readable SMS message block.
    Kept short to fit within SMS character budgets.
    """
    lines = []

    # Name — mark events clearly
    if resource.get("event_date"):
        lines.append(f"{s(lang, 'event_prefix')}{resource['name']} ({resource['event_date']})")
    else:
        lines.append(resource["name"])

    # Address
    if resource.get("address"):
        lines.append(resource["address"])

    # Phone
    if resource.get("phone"):
        lines.append(f"{s(lang, 'phone_prefix')}{resource['phone']}")

    # Hours
    if resource.get("hours"):
        lines.append(f"{s(lang, 'hours_prefix')}{resource['hours']}")

    # Walk-in flag
    if resource.get("walk_in"):
        lines.append(s(lang, "walkin_label"))

    # Notes (eligibility, special instructions, etc.)
    if resource.get("notes"):
        lines.append(resource["notes"])

    return "\n".join(lines)
