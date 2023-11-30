import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "randome.coffee@gmail.com"
receiver_email = "randome.coffee@gmail.com"
subject = "Test"
body = "Test 2"

# Create the MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the body to the email
message.attach(MIMEText(body, "plain"))

# SMTP server configuration (for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "randome.coffee@gmail.com"
smtp_password = "jeship-febkeH-mifbo8"

# Establish a connection to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Start TLS for security

# Login to your email account
server.login(smtp_username, smtp_password)

# Send the email
server.sendmail(sender_email, receiver_email, message.as_string())

# Quit the server
server.quit()
