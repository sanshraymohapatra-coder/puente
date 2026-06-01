"""
seed.py — Puente
Seeds the database with real free/low-cost health resources
in the Phoenix metropolitan area.

Run directly:  python seed.py
"""

from database import init_db, get_db

RESOURCES = [

    # ── General care ──────────────────────────────────────────────────────────

    {
        "name":      "Adelante Healthcare – Mesa",
        "address":   "1705 W Main St, Mesa AZ 85201",
        "phone":     "(480) 964-0048",
        "category":  "general",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   1,
        "notes":     "You pay based on what you can afford. Everyone is welcome, with or without insurance.",
        "zip_codes": "85201,85202,85203,85204",
    },
    {
        "name":      "Adelante Healthcare – Phoenix",
        "address":   "3033 N Central Ave, Phoenix AZ 85012",
        "phone":     "(602) 685-4200",
        "category":  "general",
        "hours":     "Mon-Fri 7:30am-5:30pm",
        "languages": "English, Spanish",
        "walk_in":   1,
        "notes":     "You pay based on what you can afford. No insurance needed. Medicaid also accepted.",
        "zip_codes": "85012,85013,85014,85015",
    },
    {
        "name":      "Mountain Park Health Center",
        "address":   "1313 E Osborn Rd, Phoenix AZ 85014",
        "phone":     "(602) 243-7277",
        "category":  "general",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Cost is based on your income. Call first to make an appointment.",
        "zip_codes": "85014,85016,85018,85020",
    },
    {
        "name":      "Valle del Sol – Primary Care",
        "address":   "4704 N Central Ave, Phoenix AZ 85012",
        "phone":     "(602) 258-6797",
        "category":  "general",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Medical care and mental health support in one place. No insurance needed.",
        "zip_codes": "85012,85013,85014,85015,85016",
    },
    {
        "name":      "Valleywise Community Health Center – South Phoenix",
        "address":   "3030 E Roosevelt St, Phoenix AZ 85008",
        "phone":     "(602) 916-7700",
        "category":  "general",
        "hours":     "Mon-Fri 7am-5pm, Sat 8am-12pm",
        "languages": "English, Spanish",
        "walk_in":   1,
        "notes":     "Cost is based on your income. No insurance needed.",
        "zip_codes": "85008,85006,85004,85034,85040",
    },
    {
        "name":      "Desert Mission Neighborhood Health Center",
        "address":   "9229 N 3rd St, Phoenix AZ 85020",
        "phone":     "(602) 870-4100",
        "category":  "general",
        "hours":     "Mon-Thu 8am-8pm, Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   1,
        "notes":     "Everyone is welcome, with or without insurance. Staff can help with translation.",
        "zip_codes": "85020,85021,85022,85023,85024",
    },
    {
        "name":      "Native Health Phoenix",
        "address":   "4520 N Central Ave, Phoenix AZ 85012",
        "phone":     "(602) 279-5262",
        "category":  "general",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Navajo, Spanish",
        "walk_in":   0,
        "notes":     "Serves all patients. Staff experienced with many cultures and backgrounds. Cost is based on your income.",
        "zip_codes": "85012,85013,85014,85015",
    },

    # ── Dental ────────────────────────────────────────────────────────────────

    {
        "name":      "A.T. Still University Dental School",
        "address":   "5850 E Still Cir, Mesa AZ 85206",
        "phone":     "(480) 219-6000",
        "category":  "dental",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Run by dental students supervised by licensed dentists. Lower-cost care for all. You must call ahead to make an appointment.",
        "zip_codes": "85201,85202,85203,85204,85205,85206,85207",
    },
    {
        "name":      "Mountain Park Health Center – Dental",
        "address":   "1313 E Osborn Rd, Phoenix AZ 85014",
        "phone":     "(602) 243-7277",
        "category":  "dental",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Cost is based on your income. Call first to make an appointment.",
        "zip_codes": "85014,85016,85018,85020",
    },
    {
        "name":      "Adelante Healthcare – Dental",
        "address":   "1705 W Main St, Mesa AZ 85201",
        "phone":     "(480) 964-0048",
        "category":  "dental",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Full dental care. You pay based on what you can afford.",
        "zip_codes": "85201,85202,85203,85204",
    },

    # ── Vision ────────────────────────────────────────────────────────────────

    {
        "name":      "Arizona College of Optometry Clinic",
        "address":   "1625 W Fountainhead Pkwy, Tempe AZ 85282",
        "phone":     "(480) 222-2828",
        "category":  "vision",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Lower-cost eye exams and eyeglasses. Adults and children welcome. You must call ahead to make an appointment.",
        "zip_codes": "85281,85282,85283,85284",
    },
    {
        "name":      "Lions Eyeglass Recycling Program – Phoenix",
        "address":   "Call for pickup location",
        "phone":     "(602) 277-5072",
        "category":  "vision",
        "hours":     "Call for availability",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Free recycled eyeglasses for people who cannot afford new ones.",
        "zip_codes": "850,851,852",
    },

    # ── Medications ───────────────────────────────────────────────────────────

    {
        "name":      "NeedyMeds Drug Assistance Programs",
        "address":   "Online / Phone",
        "phone":     "(800) 503-6897",
        "category":  "medications",
        "hours":     "24/7 online, hotline Mon-Fri 9am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Connects uninsured patients to hundreds of free and low-cost drug programs.",
        "zip_codes": "all",
    },
    {
        "name":      "Valleywise Health – 340B Pharmacy",
        "address":   "2601 E Roosevelt St, Phoenix AZ 85008",
        "phone":     "(602) 916-7900",
        "category":  "medications",
        "hours":     "Mon-Fri 8am-6pm, Sat 9am-1pm",
        "languages": "English, Spanish",
        "walk_in":   1,
        "notes":     "Very low-cost pharmacy. Much lower prices than regular pharmacies.",
        "zip_codes": "85008,85006,85004,85034",
    },
    {
        "name":      "Arizona Helps Patient Assistance",
        "address":   "Online at azhelps.org",
        "phone":     "(800) 377-1131",
        "category":  "medications",
        "hours":     "Mon-Fri 9am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Statewide program connecting Arizona residents to free brand-name medications.",
        "zip_codes": "all",
    },

    # ── Mental health ─────────────────────────────────────────────────────────

    {
        "name":      "Valle del Sol – Behavioral Health",
        "address":   "4704 N Central Ave, Phoenix AZ 85012",
        "phone":     "(602) 258-6797",
        "category":  "mental_health",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Cost is based on your income. No insurance needed.",
        "zip_codes": "85012,85013,85014,85015,85016",
    },
    {
        "name":      "La Frontera EMPACT – Crisis Line",
        "address":   "Serving all of Maricopa County",
        "phone":     "(480) 784-1500",
        "category":  "mental_health",
        "hours":     "24/7",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Free 24-hour crisis counseling by phone. No insurance required.",
        "zip_codes": "all",
    },
    {
        "name":      "Southwest Behavioral and Health Services",
        "address":   "3450 N 3rd Ave, Phoenix AZ 85013",
        "phone":     "(602) 233-3000",
        "category":  "mental_health",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   1,
        "notes":     "Behavioral health services. Cost is based on your income. If you are in crisis, you can walk in without an appointment.",
        "zip_codes": "85013,85014,85015,85004,85003",
    },

    # ── Cancer screenings ─────────────────────────────────────────────────────

    {
        "name":      "ACS Free Cancer Screening – Maricopa",
        "address":   "2929 E Thomas Rd, Phoenix AZ 85016",
        "phone":     "(602) 224-0524",
        "category":  "cancer",
        "hours":     "Call for current schedule",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Free breast, cervical, and colorectal screenings for uninsured patients. May be free if your income is low.",
        "zip_codes": "all",
    },
    {
        "name":      "Susan G. Komen AZ – Mobile Mammography",
        "address":   "Rotates locations across Phoenix metro",
        "phone":     "(480) 467-8200",
        "category":  "cancer",
        "hours":     "Call or visit komenarizontaaz.org for schedule",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Free mammograms for women 40 and older who don't have insurance or have limited coverage.",
        "zip_codes": "all",
    },
    {
        "name":      "Adelante Healthcare – Cervical Cancer Screening",
        "address":   "3033 N Central Ave, Phoenix AZ 85012",
        "phone":     "(602) 685-4200",
        "category":  "cancer",
        "hours":     "Mon-Fri 7:30am-5:30pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Free cervical cancer testing through the Well Woman Healthcheck Program.",
        "zip_codes": "85012,85013,85014,85015",
    },

    # ── Women's health ────────────────────────────────────────────────────────

    {
        "name":      "Planned Parenthood – Phoenix East",
        "address":   "1850 E Thomas Rd, Phoenix AZ 85016",
        "phone":     "(602) 277-7526",
        "category":  "womens",
        "hours":     "Mon-Sat 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   1,
        "notes":     "You pay based on what you can afford. Testing for infections, birth control, help finding prenatal care.",
        "zip_codes": "85016,85014,85018,85008",
    },
    {
        "name":      "Maricopa County – Title X Family Planning",
        "address":   "1414 W Broadway Rd, Tempe AZ 85282",
        "phone":     "(480) 784-0909",
        "category":  "womens",
        "hours":     "Mon-Fri 8am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Free or low-cost family planning for patients with low income.",
        "zip_codes": "85281,85282,85283,85284",
    },
    {
        "name":      "Valleywise Health – Women's Health",
        "address":   "2601 E Roosevelt St, Phoenix AZ 85008",
        "phone":     "(602) 916-7700",
        "category":  "womens",
        "hours":     "Mon-Fri 7am-5pm",
        "languages": "English, Spanish",
        "walk_in":   0,
        "notes":     "Women's health care, prenatal, and care after birth. Cost is based on your income.",
        "zip_codes": "85008,85006,85004,85034",
    },

    # ── Sample upcoming event (update the date before going live) ─────────────
    {
        "name":       "Free Health Fair – South Phoenix",
        "address":    "South Mountain Community Center, 212 E Alta Vista Rd, Phoenix AZ 85042",
        "phone":      "(602) 243-7277",
        "category":   "general",
        "hours":      "9am - 2pm",
        "languages":  "English, Spanish",
        "walk_in":    1,
        "notes":      "Free screenings: blood pressure, glucose, dental, vision. No appointment needed.",
        "event_date": "2025-09-20",
        "zip_codes":  "85040,85042,85044,85048",
    },
]


def seed():
    init_db()
    conn = get_db()
    c = conn.cursor()

    # Clear existing resources so re-running seed is safe
    c.execute("DELETE FROM resources")

    for r in RESOURCES:
        c.execute("""
            INSERT INTO resources
                (name, address, phone, category, hours, languages, walk_in,
                 notes, active, event_date, zip_codes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?)
        """, (
            r["name"], r.get("address"), r.get("phone"), r["category"],
            r.get("hours"), r.get("languages", "English"),
            int(r.get("walk_in", 0)), r.get("notes"),
            r.get("event_date"), r.get("zip_codes"),
        ))

    conn.commit()
    conn.close()
    print(f"Seeded {len(RESOURCES)} resources.")


if __name__ == "__main__":
    seed()
