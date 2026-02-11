#!/usr/bin/env python3
"""Send a test email via SMTP to the demo mail server."""

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello! This is a plain text test email for Suricata inspection.")
msg["Subject"] = "Test Email"
msg["From"] = "alice@example.com"
msg["To"] = "bob@example.com"

print(f"Connecting to SMTP server localhost:587 ...")
with smtplib.SMTP("localhost", 587) as s:
    s.ehlo()
    s.login("alice", "password")
    print(f"Authenticated as: alice")
    print(f"From:    {msg['From']}")
    print(f"To:      {msg['To']}")
    print(f"Subject: {msg['Subject']}")
    s.send_message(msg)

print("Mail sent successfully.")
