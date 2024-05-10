import logging

from django.core.mail import send_mail

from Ecom.celery import app

logger = logging.getLogger(__name__)


@app.task
def send_mail_to_seller(title, email):
    """
    send mail to seller email which is attached on User model.
    """
    subject = "Product Creation"
    message = f"A new product {title} has been created successfully."
    send_to = "bappi142434@gmail.com"
    recipient_list = [email]
    """
    working well with celery, currently i have not implemented
    any mail server thats why i have commented out this line
    of code
    """
    # send_mail(subject, message, send_to, recipient_list)

    logger.debug("Mail has sent.")
