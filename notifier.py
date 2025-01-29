import smtplib
from email.mime.text import MIMEText

class Notifier:
    def __init__(self, email_sender, email_password, smtp_server="smtp.gmail.com", smtp_port=587):
        self.email_sender = email_sender
        self.email_password = email_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient, subject, message):
        """Skickar ett larm via e-post."""
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self.email_sender
        msg['To'] = recipient

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_sender, self.email_password)
            server.sendmail(self.email_sender, recipient, msg.as_string())
            server.quit()
            print(f"🔔 Larm skickat till {recipient}!")
        except Exception as e:
            print(f"❌ Misslyckades att skicka larm: {e}")

# Exempel på hur man skickar en notis
if __name__ == "__main__":
    notifier = Notifier("din_email@gmail.com", "din_lösenord")
    notifier.send_email("mottagare@gmail.com", "Nätverkslarm", "En dator har kopplats från nätverket!")
