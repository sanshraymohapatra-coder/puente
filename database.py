"""
database.py — Puente
Handles all database interactions: schema setup, sessions, resources, analytics.

Privacy note: sessions use a hashed phone number as the key.
The actual phone number is never stored. All analytics are aggregate only.
"""

import sqlite3
import hashlib
from datetime import datetime, timedelta

DB_PATH = "puente.db"


# ── Connection ──────────────────────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ── Schema ───────────────────────────────────────────────────────────────────

def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            address     TEXT,
            phone       TEXT,
            category    TEXT    NOT NULL,
            hours       TEXT,
            languages   TEXT    DEFAULT 'English',
            walk_in     INTEGER DEFAULT 0,
            notes       TEXT,
            active      INTEGER DEFAULT 1,
            event_date  TEXT,
            zip_codes   TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            session_key TEXT PRIMARY KEY,
            step        TEXT    DEFAULT 'start',
            category    TEXT,
            language    TEXT    DEFAULT 'en',
            zip_code    TEXT,
            last_offset INTEGER DEFAULT 0,
            updated_at  TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS analytics (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            date        TEXT,
            category    TEXT,
            zip_prefix  TEXT,
            created_at  TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized.")


# ── Session management ────────────────────────────────────────────────────────

def make_session_key(phone_number: str) -> str:
    """
    One-way hash of the phone number.
    Lets us track session state without ever storing the phone number itself.
    """
    return hashlib.sha256(phone_number.encode()).hexdigest()[:24]


def get_session(key: str):
    conn = get_db()
    c = conn.cursor()
    # Expire sessions older than 30 minutes
    cutoff = (datetime.now() - timedelta(minutes=30)).isoformat()
    c.execute("DELETE FROM sessions WHERE updated_at < ?", (cutoff,))
    c.execute("SELECT * FROM sessions WHERE session_key = ?", (key,))
    row = c.fetchone()
    conn.commit()
    conn.close()
    return dict(row) if row else None


def save_session(key: str, step: str, category: str = None,
                 language: str = "en", zip_code: str = None, offset: int = 0):
    conn = get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()
    c.execute("""
        INSERT INTO sessions (session_key, step, category, language, zip_code, last_offset, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(session_key) DO UPDATE SET
            step        = excluded.step,
            category    = excluded.category,
            language    = excluded.language,
            zip_code    = excluded.zip_code,
            last_offset = excluded.last_offset,
            updated_at  = excluded.updated_at
    """, (key, step, category, language, zip_code, offset, now))
    conn.commit()
    conn.close()


def delete_session(key: str):
    conn = get_db()
    c = conn.cursor()
    c.execute("DELETE FROM sessions WHERE session_key = ?", (key,))
    conn.commit()
    conn.close()


# ── Resource queries ──────────────────────────────────────────────────────────

def get_resources(category: str, zip_code: str = None,
                  offset: int = 0, limit: int = 3):
    """
    Returns (results_list, has_more_bool).
    Events are surfaced first (sorted by date), then regular resources alphabetically.
    """
    conn = get_db()
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")

    # Upcoming events for this category
    if category == "all":
        c.execute("""
            SELECT * FROM resources
            WHERE active = 1 AND event_date IS NOT NULL AND event_date >= ?
            ORDER BY event_date ASC
        """, (today,))
    else:
        c.execute("""
            SELECT * FROM resources
            WHERE active = 1 AND category = ? AND event_date IS NOT NULL AND event_date >= ?
            ORDER BY event_date ASC
        """, (category, today))
    events = [dict(r) for r in c.fetchall()]

    # Regular (non-event) resources
    if category == "all":
        c.execute("""
            SELECT * FROM resources
            WHERE active = 1 AND event_date IS NULL
            ORDER BY category, name ASC
        """)
    else:
        c.execute("""
            SELECT * FROM resources
            WHERE active = 1 AND category = ? AND event_date IS NULL
            ORDER BY name ASC
        """, (category,))
    regulars = [dict(r) for r in c.fetchall()]

    conn.close()

    all_resources = events + regulars
    page = all_resources[offset : offset + limit]
    has_more = len(all_resources) > offset + limit
    return page, has_more


# ── Analytics ─────────────────────────────────────────────────────────────────

def log_analytic(category: str, zip_code: str):
    """
    Logs aggregate usage data only.
    Zip is stored as a 3-digit prefix (e.g. '850') — not the full zip.
    No phone number, no session ID, no personal data.
    """
    conn = get_db()
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    zip_prefix = zip_code[:3] if zip_code and len(zip_code) >= 3 else "unknown"
    c.execute("""
        INSERT INTO analytics (date, category, zip_prefix, created_at)
        VALUES (?, ?, ?, ?)
    """, (today, category, zip_prefix, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def get_analytics_summary():
    """Returns a summary dict for the admin dashboard (future use)."""
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) as total FROM analytics")
    total = c.fetchone()["total"]
    c.execute("""
        SELECT category, COUNT(*) as count
        FROM analytics GROUP BY category ORDER BY count DESC
    """)
    by_category = {row["category"]: row["count"] for row in c.fetchall()}
    conn.close()
    return {"total_sessions": total, "by_category": by_category}
