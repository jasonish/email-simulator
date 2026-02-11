#!/usr/bin/env python3
"""Read emails via IMAP from the demo mail server."""

import imaplib
import email

print("Connecting to IMAP server localhost:1143 ...")
m = imaplib.IMAP4("localhost", 1143)
m.login("bob@example.com", "password")
print("Authenticated as: bob@example.com")
m.select("INBOX")

typ, data = m.search(None, "ALL")
nums = data[0].split()

if not nums:
    print("No messages in INBOX.")
else:
    print(f"Found {len(nums)} message(s) in INBOX.\n")
    for num in nums:
        typ, msg_data = m.fetch(num, "(RFC822)")
        raw = msg_data[0][1]
        parsed = email.message_from_bytes(raw)
        print(f"--- Message {num.decode()} ---")
        print(f"From:    {parsed['From']}")
        print(f"To:      {parsed['To']}")
        print(f"Subject: {parsed['Subject']}")
        print(f"Body:    {parsed.get_payload(decode=True).decode()}")
        print()

m.logout()
print("Done.")
