import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from langchain.tools import StructuredTool

def send_gmail(recipient: str, subject: str, body: str, attachment_path: str = None):
    """
    Send an email using Gmail's SMTP server.

    :param recipient: The recipient's email address.
    :param subject: The subject of the email.
    :param body: The body of the email.
    :param attachment_path: Optional path to a .txt file to attach.
    """
    email_address = 'agenthummus@gmail.com'
    email_password = 'mmbb fyln klcc bxnz'  # Replace with environment variable or secure method
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Use 465 for SSL

    # Create a MIMEMultipart email message
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Check for attachment
    if attachment_path:
        # Make sure the file exists
        if os.path.isfile(attachment_path):
            with open(attachment_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(attachment_path)}',
                )
                msg.attach(part)
        else:
            print(f"The specified attachment path {attachment_path} does not exist.")

    # Establish a secure session with the server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)
sendgmailtool =  StructuredTool.from_function(send_gmail)

def create_text_file(filename: str, content: str) -> None:
    """
    Create a new text file with the given filename and write the provided content to it.
    
    :param filename: The name of the file to create.
    :param content: The content to write to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)
maketxttool = StructuredTool.from_function(create_text_file)