import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

gmail_user = "yourmail@gmail.com"
# enter gmail app pasword that you have generated here
gmail_password = "gmail_app_password"


def read_contacts(path):
    contacts = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            email, name = line.strip().split(";")
            contacts.append((email, name))

    return contacts


def create_email(to_email, to_name, encoded_cv_part):
    subject = "(Replace with subject)"
    body = """\
    
    (Replace this with internship mail body)
    
    """

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the email body
    msg.attach(MIMEText(body, "plain", "utf-8"))
    # Attach the pre-encoded CV part (reusing the same encoded part)
    msg.attach(encoded_cv_part)

    return msg


# Function to encode the CV once and reuse it
def encode_cv(cv_file):
    with open(cv_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={cv_file}")
    return part


# Send the emails with the pre-encoded CV
def send_emails(contacts, encoded_cv_part):
    try:
        # Establish connection with Gmail server
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(gmail_user, gmail_password)

        for email, name in contacts:
            try:
                msg = create_email(email, name, encoded_cv_part)
                server.sendmail(gmail_user, email, msg.as_string())
                print(f"Email sent to {name} at {email}")
            except Exception as ex:
                print(f"Failed to send to {name} at {email}, Error: {ex}")

        server.quit()
    except Exception as e:
        print(f"Failed to connect to gmail server. Error: {e}")


# Main flow
contacts = read_contacts("contacts.txt")
encoded_cv_part = encode_cv("replace_with_cv_name.pdf")  # Encode CV only once
send_emails(contacts, encoded_cv_part)
