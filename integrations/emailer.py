import os, requests

BREVO_API_KEY = os.getenv("BREVO_API_KEY")

def send_followup_email(to_email, subject, html):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {"api-key": BREVO_API_KEY, "Content-Type": "application/json"}
    payload = {
        "sender": {"email":"you@example.com"},
        "to":[{"email": to_email}],
        "subject": subject,
        "htmlContent": html
    }
    r = requests.post(url, headers=headers, json=payload)
    r.raise_for_status()
    return r.json()
