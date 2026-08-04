from email.message import EmailMessage

email = EmailMessage()

email["From"] = "sender@example.com"
email["To"] = "receiver@example.com"
email["Subject"] = "Python Email Module"

email.set_content("Hello! This is a test email.")

print(email)