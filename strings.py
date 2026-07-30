"""
strings.py — Puente
All user-facing text in English (en), Spanish (es), Farsi (fa), and Hindi (hi).
To add a new language, duplicate one of the language blocks and translate.

NOTE on SMS encoding: Farsi and Hindi use non-Latin scripts, which forces
UCS-2 encoding on SMS (70 chars/segment instead of 160). Keep those strings
as concise as practical. The app sends multi-segment messages automatically —
we just want to avoid unnecessary verbosity.
"""

# ── All response strings ──────────────────────────────────────────────────────

STRINGS = {
    "en": {
        "welcome": (
            "Hi! I'm Puente — I'll help you find free health resources nearby.\n\n"
            "What do you need?\n\n"
            "1 – General care\n"
            "2 – Dental\n"
            "3 – Vision\n"
            "4 – Medications\n"
            "5 – Mental health\n"
            "6 – Cancer screenings\n"
            "7 – Women's health\n"
            "8 – All resources\n\n"
            "Para Español: ES | فارسی: FA | हिंदी: HINDI"
        ),
        "ask_zip": (
            "Got it. What's your zip code?\n\n"
            "(We use this only to find nearby resources — we never save it.)"
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
        "invalid_choice": "Please reply with a number 1–8 to choose a category.",
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
            "— we never save it.)"
        ),
        "cat_general":       "general health care",
        "cat_dental":        "dental care",
        "cat_vision":        "vision care",
        "cat_medications":   "help with medications",
        "cat_mental_health": "mental health support",
        "cat_cancer":        "cancer screenings",
        "cat_womens":        "women's health care",
        "cat_all":           "health resources",
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
            "Hola! Soy Puente — te ayudo a encontrar recursos de salud gratuitos.\n\n"
            "Que necesitas?\n\n"
            "1 – Atencion general\n"
            "2 – Dental\n"
            "3 – Vision\n"
            "4 – Medicamentos\n"
            "5 – Salud mental\n"
            "6 – Examenes de cancer\n"
            "7 – Salud de la mujer\n"
            "8 – Todos los recursos\n\n"
            "For English: EN | فارسی: FA | हिंदी: HINDI"
        ),
        "ask_zip": (
            "Entendido. Cual es tu codigo postal?\n\n"
            "(Solo lo usamos para encontrar recursos cercanos — nunca lo guardamos.)"
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
        "cat_general":       "atencion medica general",
        "cat_dental":        "atencion dental",
        "cat_vision":        "atencion de la vista",
        "cat_medications":   "ayuda con medicamentos",
        "cat_mental_health": "apoyo de salud mental",
        "cat_cancer":        "examenes de cancer",
        "cat_womens":        "salud de la mujer",
        "cat_all":           "recursos de salud",
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

    # ── Farsi / Persian (فارسی) ─────────────────────────────────────────────────
    # Trigger words: FA, FARSI, PERSIAN, فارسی
    # Script: Arabic/Persian — RTL, UCS-2 SMS encoding (70 chars per segment)
    # IMPORTANT: These translations should be reviewed by a native Farsi speaker
    # before clinical use.
    "fa": {
        "welcome": (
            "سلام! من Puente هستم — منابع بهداشتی رایگان نزدیک شما را پیدا می‌کنم.\n\n"
            "به چه کمکی نیاز دارید؟\n\n"
            "1 – مراقبت عمومی\n"
            "2 – دندانپزشکی\n"
            "3 – بینایی\n"
            "4 – داروها\n"
            "5 – سلامت روان\n"
            "6 – غربالگری سرطان\n"
            "7 – بهداشت زنان\n"
            "8 – همه منابع\n\n"
            "For English: EN | Para Español: ES | हिंदी: HINDI"
        ),
        "ask_zip": (
            "متوجه شدم. کد پستی شما چیست؟\n\n"
            "(فقط برای یافتن منابع نزدیک استفاده می‌کنیم — هرگز ذخیره نمی‌شود.)"
        ),
        "results_header": "در نزدیکی {zip}، {count} گزینه رایگان وجود دارد:\n",
        "walk_in": "بدون وقت قبلی",
        "more_prompt": "\nبرای نتایج بیشتر MORE بفرستید، یا برای جستجوی دوباره START.",
        "no_more": "\nبرای جستجوی دوباره START بفرستید.",
        "no_results": (
            "هنوز منابعی برای این منطقه نداریم.\n\n"
            "یک کد پستی نزدیک امتحان کنید یا START بفرستید."
        ),
        "invalid_zip": (
            "کد پستی معتبر نیست.\n\n"
            "لطفاً کد پستی 5 رقمی بفرستید (مثلاً 85034)."
        ),
        "invalid_choice": "لطفاً عددی بین 1 تا 8 بفرستید.",
        "freetext_nomatch": (
            "مطمئن نیستم چطور کمک کنم. یک عدد بفرستید:\n\n"
            "1 - مراقبت عمومی\n"
            "2 - دندانپزشکی\n"
            "3 - بینایی\n"
            "4 - داروها\n"
            "5 - سلامت روان\n"
            "6 - غربالگری سرطان\n"
            "7 - بهداشت زنان\n"
            "8 - همه موارد"
        ),
        "freetext_match": (
            "به نظر می‌رسد به {category} نیاز دارید.\n\n"
            "کد پستی شما چیست؟ (هرگز ذخیره نمی‌شود.)"
        ),
        "cat_general":       "مراقبت بهداشتی عمومی",
        "cat_dental":        "دندانپزشکی",
        "cat_vision":        "بینایی",
        "cat_medications":   "کمک با داروها",
        "cat_mental_health": "حمایت سلامت روان",
        "cat_cancer":        "غربالگری سرطان",
        "cat_womens":        "بهداشت زنان",
        "cat_all":           "منابع بهداشتی",
        "help": (
            "Puente به شما کمک می‌کند منابع بهداشتی رایگان را پیدا کنید.\n\n"
            "برای جستجوی جدید START بفرستید.\n"
            "برای توقف پیام‌ها STOP بفرستید."
        ),
        "stop": "لغو اشتراک شدید. هر زمان برای جستجو پیام دهید.",
        "start_prefix": "خوش آمدید! ",
        "event_prefix": "رویداد ",
        "hours_prefix": "ساعات: ",
        "phone_prefix": "تماس: ",
        "walkin_label": "بدون نیاز به وقت قبلی — فقط بیایید",
        "notes_prefix": "",
    },

    # ── Hindi (हिंदी) ──────────────────────────────────────────────────────────
    # Trigger words: HINDI, हिंदी
    # Note: "HI" is already in START_WORDS (English greeting), so we use "HINDI".
    # Script: Devanagari — UCS-2 SMS encoding (70 chars per segment)
    # IMPORTANT: These translations should be reviewed by a native Hindi speaker
    # before clinical use.
    "hi": {
        "welcome": (
            "नमस्ते! मैं Puente हूँ — आपके पास मुफ़्त स्वास्थ्य सेवाएं खोजने में मदद करूँगा.\n\n"
            "आपको क्या चाहिए?\n\n"
            "1 – सामान्य देखभाल\n"
            "2 – दंत चिकित्सा\n"
            "3 – आँखों की देखभाल\n"
            "4 – दवाइयां\n"
            "5 – मानसिक स्वास्थ्य\n"
            "6 – कैंसर जांच\n"
            "7 – महिला स्वास्थ्य\n"
            "8 – सभी संसाधन\n\n"
            "For English: EN | Para Español: ES | فارسی: FA"
        ),
        "ask_zip": (
            "समझ गया. आपका ज़िप कोड क्या है?\n\n"
            "(हम इसे केवल पास के संसाधन खोजने के लिए उपयोग करते हैं — कभी सहेजते नहीं.)"
        ),
        "results_header": "{zip} के पास {count} मुफ़्त विकल्प:\n",
        "walk_in": "अपॉइंटमेंट ज़रूरी नहीं",
        "more_prompt": "\nअधिक परिणामों के लिए MORE भेजें, या फिर खोजने के लिए START.",
        "no_more": "\nफिर से खोजने के लिए START भेजें.",
        "no_results": (
            "उस क्षेत्र में अभी कोई संसाधन नहीं हैं.\n\n"
            "पास का ज़िप कोड आज़माएं या START भेजें."
        ),
        "invalid_zip": (
            "यह वैध ज़िप कोड नहीं लगता.\n\n"
            "कृपया 5 अंकों का ज़िप कोड भेजें (जैसे 85034)."
        ),
        "invalid_choice": "कृपया 1-8 के बीच कोई संख्या भेजें.",
        "freetext_nomatch": (
            "मुझे समझ नहीं आया. एक संख्या भेजें:\n\n"
            "1 - सामान्य देखभाल\n"
            "2 - दंत चिकित्सा\n"
            "3 - आँखें\n"
            "4 - दवाइयां\n"
            "5 - मानसिक स्वास्थ्य\n"
            "6 - कैंसर जांच\n"
            "7 - महिला स्वास्थ्य\n"
            "8 - सब कुछ दिखाएं"
        ),
        "freetext_match": (
            "लगता है आपको {category} की ज़रूरत है.\n\n"
            "आपका ज़िप कोड क्या है? (हम कभी सहेजते नहीं.)"
        ),
        "cat_general":       "सामान्य स्वास्थ्य देखभाल",
        "cat_dental":        "दंत चिकित्सा",
        "cat_vision":        "आँखों की देखभाल",
        "cat_medications":   "दवाओं में मदद",
        "cat_mental_health": "मानसिक स्वास्थ्य सहायता",
        "cat_cancer":        "कैंसर जांच",
        "cat_womens":        "महिला स्वास्थ्य",
        "cat_all":           "स्वास्थ्य संसाधन",
        "help": (
            "Puente आपको टेक्स्ट से मुफ़्त स्वास्थ्य सेवाएं खोजने में मदद करता है.\n\n"
            "नई खोज के लिए START भेजें.\n"
            "संदेश बंद करने के लिए STOP भेजें."
        ),
        "stop": "सदस्यता रद्द हो गई. संसाधन खोजने के लिए कभी भी संदेश करें.",
        "start_prefix": "वापस स्वागत है! ",
        "event_prefix": "कार्यक्रम ",
        "hours_prefix": "समय: ",
        "phone_prefix": "कॉल करें: ",
        "walkin_label": "अपॉइंटमेंट ज़रूरी नहीं — सीधे आएं",
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
MORE_WORDS  = {"MORE", "MAS", "MÁS", "SIGUIENTE", "NEXT",
               "بیشتر",    # Farsi: bishtar
               "ادامه"}    # Farsi: edame
EN_WORDS    = {"EN", "ENGLISH"}
ES_WORDS    = {"ES", "ESPANOL", "ESPAÑOL"}
FA_WORDS    = {"FA", "FARSI", "PERSIAN",
               "فارسی"}    # فارسی
HI_WORDS    = {"HINDI",
               "हिंदी"}    # हिंदी


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



# ── Romanized-script word sets for detect_language() ─────────────────────────
# Used when a patient texts in Latin letters instead of their native script.
# Words are chosen to be unambiguous — not shared with English or Spanish.

# Finglish (romanized Farsi) — checked BEFORE Hinglish because several words
# overlap with Hindi/Urdu; unambiguous Farsi-only roots are listed first.
_FINGLISH_MARKERS = {
    # Teeth / dental
    "dandan", "dandoon",
    # Eyes
    "cheshm", "cheshmam",
    # Doctor (Farsi spelling)
    "pezeshk", "doktor",
    # "I want / I need" conjugations (unique to Farsi)
    "mikhaam", "mikham", "mikhastam", "mikhahi",
    # "I have" (unique to Farsi)
    "daram", "darim", "darand",
    # Sick / patient
    "mariz", "bimaram", "bemaram",
    # Treatment / medicine (Farsi spellings)
    "darman", "dava",
    # Where / please (unambiguous Farsi)
    "koja", "lotfan", "kheili",
    # Common Farsi sentence words
    "mishe", "nemitonam", "nemishe", "bekhatir",
    # Pain (shared with Hindi but used in Finglish health phrases)
    "dardm", "dardesh",
}

# Hinglish (romanized Hindi) — common health-related and everyday words that
# are unambiguous and won't appear in English or Spanish.
_HINGLISH_MARKERS = {
    # Negation
    "nahi", "nahin", "mat",
    # Need / want
    "chahiye", "chaiye", "chahta", "chahti",
    # I / my
    "mujhe", "muje", "mera", "meri", "mere", "humara", "humari",
    # Illness / pain
    "bimari", "beemari", "takleef", "pareshani", "dard",
    # Body parts (Hindi) — note: "pet" (stomach) and "sir" (head) removed
    # because they are common English words that cause false positives
    "dant", "daant", "aankh", "aankhon",
    # Medicine
    "dawai", "dawa", "aushadhi", "ilaj",
    # Fever / cough / cold
    "bukhar", "khansi", "nazla", "zukam",
    # Quantity / degree
    "thoda", "bahut", "zyada", "kuch",
    # Question / common Hindi words
    "kya", "kahan", "kaise", "kyun", "kitna",
    # Health
    "sehat", "swasthya", "tandrust",
    # Pregnancy / women
    "garbhavati", "prasav",
    # Common Hinglish sentence words — "mat", "ho" removed (English words)
    "hai", "hain", "tha", "thi", "kar", "karo", "karna",
    "sakte", "sakti", "raha", "rahi",
}


def detect_language(text: str) -> str:
    """
    Detect language from a patient's first message.
    Checks native scripts first (definitive), then romanized-script word lists
    (Finglish before Hinglish to handle overlapping roots), then Spanish.
    Defaults to English when ambiguous.
    """
    # ── Native script detection (definitive) ────────────────────────────────
    # Farsi/Arabic script: Unicode block U+0600–U+06FF
    if any('؀' <= c <= 'ۿ' for c in text):
        return "fa"

    # Devanagari script / Hindi: Unicode block U+0900–U+097F
    if any('ऀ' <= c <= 'ॿ' for c in text):
        return "hi"

    t = text.lower().strip()
    words = set(t.split())

    # ── Single-word trigger shortcuts ────────────────────────────────────────
    if t in {"es", "español", "espanol", "hola", "ayuda", "inicio", "alto", "mas"}:
        return "es"
    if t in {"en", "english", "hi", "hello", "help", "start", "stop", "more"}:
        return "en"

    # ── Romanized Farsi (Finglish) ───────────────────────────────────────────
    # Require 1 unambiguous Finglish marker to avoid false positives.
    if words & _FINGLISH_MARKERS:
        return "fa"

    # ── Romanized Hindi (Hinglish) ───────────────────────────────────────────
    # Require 1 unambiguous Hinglish marker.
    if words & _HINGLISH_MARKERS:
        return "hi"

    # ── Spanish word detection ───────────────────────────────────────────────
    spanish_markers = {
        "que", "por", "para", "gracias", "como", "donde",
        "salud", "medico", "clinica", "clínica", "necesito",
        "tengo", "busco", "gratis", "ayuda", "favor",
    }
    if words & spanish_markers:
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
