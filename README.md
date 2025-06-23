# SMTP Email Verifier

This Python script uses DNS and SMTP to verify whether an email address is deliverable. It performs an SMTP handshake to the target domain's mail server and checks the validity of the recipient address using `RCPT TO`.

⚠️ Note: Some modern mail servers block this kind of verification, so results may not always be accurate.

---

## 🧠 Function Overview

```python
import smtplib
import dns.resolver

def verify_email(email):
    domain = email.split('@')[1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
        server = smtplib.SMTP(timeout=10)
        server.connect(mx_record)
        server.helo("example.com")
        server.mail("you@example.com")
        code, message = server.rcpt(email)
        server.quit()
        return code == 250
    except:
        return False
```

---

## 🚀 Usage

1. Save the script as `verify_email.py`
2. Run in Python:
```python
from verify_email import verify_email

print(verify_email("test@example.com"))  # Output: True or False
```

---

## 📦 Requirements

- Python 3+
- `dnspython` for MX lookup

### Install dependencies:
```bash
pip install dnspython
```

---

## ⚠️ Limitations

- Many mail servers block or silently accept all RCPT commands, making verification unreliable.
- This method does not send real emails but can trigger rate limits or bans on aggressive usage.

---

## 🛡️ Disclaimer

This tool is for educational and ethical use only. Do not use to spam, harass, or probe without permission.
