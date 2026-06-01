"""
app.py — Puente
Flask application. Exposes a single POST /sms webhook that Twilio calls
whenever a patient texts the Puente number.
"""

import os
from flask import Flask, request, abort, render_template, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
from dotenv import load_dotenv

from database import init_db
from handler import handle_message

load_dotenv()

app = Flask(__name__)
# Trust X-Forwarded-Proto from ngrok/Railway so request.url uses https://
# which must match the URL Twilio signed the request with.
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")


# ── Webhook ───────────────────────────────────────────────────────────────────

@app.route("/sms", methods=["POST"])
def sms_webhook():
    """
    Twilio calls this endpoint every time someone texts the Puente number.
    We validate the request came from Twilio, route it through the handler,
    and respond with TwiML.
    """

    # Validate the request is genuinely from Twilio (skip in dev if no token set)
    if TWILIO_AUTH_TOKEN:
        validator = RequestValidator(TWILIO_AUTH_TOKEN)
        signature = request.headers.get("X-Twilio-Signature", "")
        url = request.url
        params = request.form.to_dict()
        if not validator.validate(url, params, signature):
            abort(403)

    body         = request.form.get("Body", "").strip()
    from_number  = request.form.get("From", "")

    # Route through core logic
    reply_text = handle_message(body, from_number)

    # Wrap in TwiML
    resp = MessagingResponse()
    resp.message(reply_text)
    return str(resp), 200, {"Content-Type": "text/xml"}


# ── Health check (useful for Railway/Render uptime monitoring) ─────────────────

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok", "service": "Puente"}, 200


# ── Analytics endpoint (simple admin view, no patient data) ───────────────────

@app.route("/analytics", methods=["GET"])
def analytics():
    from database import get_analytics_summary
    return get_analytics_summary(), 200


# ── Demo UI ───────────────────────────────────────────────────────────────────

@app.route("/demo", methods=["GET"])
def demo():
    return render_template("demo.html")


@app.route("/demo/message", methods=["POST"])
def demo_message():
    data = request.get_json(force=True)
    body       = data.get("body", "").strip()
    session_id = data.get("session_id", "demo-default")
    # Use the session_id as a fake phone number so each browser tab gets
    # its own isolated session without storing any real phone number.
    fake_phone = f"+1demo{session_id[:12]}"
    reply = handle_message(body, fake_phone)
    return jsonify({"reply": reply})


# ── Startup ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()

    # Seed the database if it's empty
    from database import get_db
    conn = get_db()
    count = conn.execute("SELECT COUNT(*) FROM resources").fetchone()[0]
    conn.close()
    if count == 0:
        print("No resources found — running seed...")
        from seed import seed
        seed()

    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV", "production") == "development"
    print(f"Puente running on port {port} (debug={debug})")
    app.run(host="0.0.0.0", port=port, debug=debug)
