"""
A simple python script to read emails from gmail and send out automated messages

NOTE : Please read the readMe.md file before using the script
"""

import os
import email
import poplib
import logging
import smtplib, ssl
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv('EMAIL')
FORWARD_MAIL_TO = os.getenv('FORWARD_MAIL_TO')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')

try:
    
    # Connecting to Gmail
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user(EMAIL)
    pop_conn.pass_(PASSWORD)
    
    mails = len(pop_conn.list()[1])
    for idx in range(mails):
        raw_email = b"\n".join(pop_conn.retr(idx + 1)[1])
        parsed_email = email.message_from_bytes(raw_email)

        port = PORT  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = EMAIL  # Enter your address
        receiver_email = parsed_email["From"] # Enter receiver address
        
        if not "@gmail.com" in receiver_email:
            continue
        
        password = PASSWORD
        
        # Feel free to change the message as needed
        message = """\
Subject: Thank you for your message

Hi there, we will inform Varun about your message

Thank you for reaching out

Note: do not reply this is a system generated email using python
"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            
        message = f"""\
Subject: {parsed_email["Subject"]}

Hi Varun, you have recieved a email from {parsed_email["From"]}

check your inbox for details
"""
        
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, FORWARD_MAIL_TO, message)
except poplib.error_proto as e:
    logging.error(e)
except Exception as e:
    logging.error(e)
finally:
    pop_conn.quit()
    