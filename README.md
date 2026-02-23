# Email Sandbox

A Docker Compose mail infrastructure for testing network traffic inspection tools like Suricata. All protocols run in plain text (no TLS/SSL). Only `@example.com` recipients are accepted.

## Quick Start

```bash
docker compose up -d
python3 send-mail.py    # alice sends a test email to bob
python3 read-mail.py    # read bob's inbox via IMAP
```

Or use mutt:

```bash
mutt -F muttrc.alice
mutt -F muttrc.bob
```

## Ports

| Service    | Container | Host Default | `.env` Variable   |
|------------|-----------|--------------|-------------------|
| SMTP       | 25        | 2525         | `SMTP_PORT`       |
| Submission | 587       | 587          | `SUBMISSION_PORT` |
| IMAP       | 143       | 1143         | `IMAP_PORT`       |
| POP3       | 110       | 1110         | `POP3_PORT`       |

Port 25 is unauthenticated (relay from Docker networks). Port 587 requires SMTP AUTH.

## Accounts

| Address             | Password   |
|---------------------|------------|
| alice@example.com   | password   |
| bob@example.com     | password   |

## Traffic Capture

Find the Docker bridge interface:

```bash
docker network inspect email-sandbox_default --format '{{.Id}}' \
  | cut -c1-12 | xargs -I{} echo "br-{}"
```

Capture on the bridge (sees container ports):

```bash
sudo tcpdump -i br-XXXXXXXXXXXX -nn -X port 25 or port 587 or port 143 or port 110
```

## Teardown

```bash
docker compose down -v   # -v removes the mail volume
```
