# Puente — SMS Health Resource Navigator
**Free. No app download. Works on any phone.**

Patients text a number, answer two questions, and receive free health resources
near them. No account. No personal data stored. Bilingual English/Spanish.

---

## What you need before starting

- A computer with Python 3.10+ installed
- A free [Twilio account](https://twilio.com/try-twilio) (~5 minutes to set up)
- A free [ngrok account](https://ngrok.com) for local testing
- (For deployment) A free [Railway](https://railway.app) account

---

## Part 1 — Run it on your computer

### Step 1: Get the code

If you downloaded a zip file, extract it. If you're using the terminal:

```bash
cd Desktop
# (the puente/ folder should already be here)
cd puente
```

### Step 2: Install Python dependencies

```bash
pip install -r requirements.txt
```

If you get a permissions error on Mac/Linux, try:
```bash
pip install -r requirements.txt --break-system-packages
```

### Step 3: Create your .env file

Copy the example file:
```bash
cp .env.example .env
```

Open `.env` in any text editor. You'll fill in the Twilio credentials in Step 5.
For now, just save it as-is — the app will run without them for local testing.

### Step 4: Start the app

```bash
python app.py
```

You should see:
```
Database initialized.
Seeded 25 resources.
Puente running on port 5000 (debug=False)
```

The app is now running at `http://localhost:5000`.

### Step 5: Test the logic (no Twilio needed)

Open a new terminal window and run:
```bash
python3 -c "
from handler import handle_message
phone = '+15555550000'
print(handle_message('hi', phone))
"
```

You should see the welcome menu printed in English. Try the full flow:
```bash
python3 -c "
from handler import handle_message
p = '+15555550001'
print(handle_message('hi', p))        # Welcome menu
print('---')
print(handle_message('1', p))         # Choose general care
print('---')
print(handle_message('85012', p))     # Send zip → get resources
print('---')
print(handle_message('more', p))      # More results
"
```

---

## Part 2 — Connect a real Twilio phone number (local testing)

### Step 6: Create a Twilio account

1. Go to [twilio.com/try-twilio](https://twilio.com/try-twilio)
2. Sign up for a free trial account
3. Verify your email and phone number
4. On the dashboard, note your **Account SID** and **Auth Token**

### Step 7: Get a phone number

1. In the Twilio console, go to **Phone Numbers → Manage → Buy a Number**
2. Search for a number with SMS capability
3. Trial accounts get one number free
4. Buy (or claim) the number

### Step 8: Add credentials to .env

Open your `.env` file and fill in:
```
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
```

Restart the app:
```bash
python app.py
```

### Step 9: Expose your local server with ngrok

ngrok creates a public URL that Twilio can reach on your local machine.

1. Download ngrok from [ngrok.com/download](https://ngrok.com/download)
2. Sign up for a free account and get your auth token
3. Run:
```bash
ngrok http 5000
```

You'll see output like:
```
Forwarding   https://abc123.ngrok-free.app -> http://localhost:5000
```

Copy that `https://` URL — you'll need it in the next step.

### Step 10: Connect Twilio to your app

1. In the Twilio console, go to **Phone Numbers → Manage → Active Numbers**
2. Click your number
3. Scroll to **Messaging Configuration**
4. Under "A message comes in", set:
   - **Webhook**: `https://abc123.ngrok-free.app/sms`
   - **HTTP Method**: POST
5. Click **Save**

### Step 11: Text your number

Send a text to your Twilio number from your phone. You should get the Puente
welcome menu back within a few seconds.

> **Note:** Twilio trial accounts can only send messages to verified phone
> numbers. Go to **Verified Caller IDs** in the console to add your number.

---

## Part 3 — Deploy to Railway (permanent, free hosting)

Once you're ready for clinics to use it, deploy to Railway so the app runs
24/7 without your computer being on.

### Step 12: Put the code on GitHub

1. Create a free [GitHub account](https://github.com) if you don't have one
2. Create a new repository called `puente`
3. Push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/puente.git
git push -u origin main
```

> **Important:** Make sure `.gitignore` is working. Your `.env` file and
> `puente.db` should NOT be committed to GitHub.

### Step 13: Deploy on Railway

1. Go to [railway.app](https://railway.app) and sign up with GitHub
2. Click **New Project → Deploy from GitHub repo**
3. Select your `puente` repository
4. Railway detects the `Procfile` and deploys automatically

### Step 14: Set environment variables on Railway

1. In your Railway project, click your service
2. Go to the **Variables** tab
3. Add these variables (same values as your `.env` file):
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `FLASK_ENV` = `production`

Click **Deploy** after adding variables.

### Step 15: Seed the database on Railway

Railway gives you a shell. In your project, click **Settings → New Service →
Railway Shell** (or use the CLI). Run:

```bash
python seed.py
```

### Step 16: Update Twilio webhook to Railway URL

1. In Railway, go to **Settings → Networking → Generate Domain**
2. Copy the generated URL (e.g. `puente.railway.app`)
3. Go back to Twilio, update the webhook to:
   `https://puente.railway.app/sms`

---

## Part 4 — Add or update resources

### Adding a resource to the database

Open `seed.py` and add a new entry to the `RESOURCES` list following this
pattern:

```python
{
    "name":      "Clinic Name",
    "address":   "123 Main St, Phoenix AZ 85001",
    "phone":     "(602) 555-0100",
    "category":  "general",       # general, dental, vision, medications,
                                  # mental_health, cancer, womens
    "hours":     "Mon-Fri 9am-5pm",
    "languages": "English, Spanish",
    "walk_in":   1,               # 1 = walk-ins welcome, 0 = appointment only
    "notes":     "Sliding scale. Uninsured welcome.",
    "zip_codes": "85001,85002,85003",
},
```

For a one-time event, add an `event_date` field:
```python
{
    ...
    "event_date": "2025-10-15",   # YYYY-MM-DD format
},
```

After editing, re-run the seed:
```bash
python seed.py
```

> This clears and re-seeds all resources. For production, you'll eventually
> want to add resources via the database directly rather than re-seeding.

### Directly editing the database (SQLite)

The database file is `puente.db`. You can open it with
[DB Browser for SQLite](https://sqlitebrowser.org) (free, visual interface)
to add, edit, or deactivate resources without touching code.

---

## Part 5 — Tracking impact

### View analytics

Visit `https://your-app-url.railway.app/analytics` in a browser.

Returns:
```json
{
  "total_sessions": 142,
  "by_category": {
    "general": 67,
    "dental": 31,
    "mental_health": 22,
    "medications": 14,
    "cancer": 8
  }
}
```

This is the data you'll use for your application and research. No patient data
is stored — only aggregate counts by category and 3-digit zip prefix.

---

## File structure

```
puente/
├── app.py          Flask app + Twilio webhook
├── handler.py      Core SMS routing logic
├── database.py     SQLite setup and queries
├── strings.py      All English and Spanish response text
├── seed.py         Phoenix resource data
├── requirements.txt
├── Procfile        Railway/Heroku deployment
├── .env.example    Credentials template
├── .gitignore
└── README.md
```

---

## Adding a new language

1. Open `strings.py`
2. Copy the entire `"en"` block, paste it as `"pt"` (Portuguese) or whatever
   the language code is
3. Translate every string value
4. In `handler.py`, add detection keywords to `ES_WORDS`-style sets
5. Update the welcome menu to include the new language option

---

## Common issues

**"Module not found" errors**
Run `pip install -r requirements.txt` again.

**Twilio says "no response" or webhook fails**
- Make sure `python app.py` is running
- Make sure ngrok is running and the URL is correct in Twilio
- Check that the webhook URL ends in `/sms`

**App runs but returns no resources for a zip code**
The zip code filtering in the MVP is broad — all Phoenix-area resources appear
for any Phoenix zip code. If you get no results, the category may have no
resources in the database. Run `python seed.py` to make sure the database is
populated.

**Railway deploy fails**
Make sure `Procfile` is in the root directory (not inside a subfolder) and
your environment variables are set in the Railway Variables tab.

---

## What's next (after MVP)

- **Clinic admin panel** — web dashboard for partner clinics to manage their
  own resources without editing code
- **WhatsApp support** — same backend, Twilio WhatsApp Business API channel
- **Additional languages** — add a language file, update detection keywords
- **Additional cities** — add resources for new metro areas in `seed.py`
