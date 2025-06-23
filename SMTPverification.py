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
