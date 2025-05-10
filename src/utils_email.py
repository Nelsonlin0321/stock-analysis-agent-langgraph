import os
import markdown2
from typing import Optional
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .utils import exponential_retry
import dotenv
dotenv.load_dotenv()
GMAIL = os.getenv("GMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


def markdown_to_html(markdown_text: str, extras: Optional[list[str]] = None) -> str:
    """
    Convert markdown text to HTML format suitable for email sending.

    Args:
        markdown_text (str): The markdown text to convert
        extras (Optional[list[str]]): Additional markdown2 features to enable.
            Default includes 'tables', 'fenced-code-blocks', and 'break-on-newline'

    Returns:
        str: HTML formatted text ready for email sending
    """
    if extras is None:
        extras = ['tables', 'fenced-code-blocks', 'break-on-newline']

    # Convert markdown to HTML
    html = markdown2.markdown(
        markdown_text,
        extras=extras
    )

    return html


@exponential_retry(retries=3, return_value_if_fail="Fail to send the email")
def send_email_gmail(subject: str, body: str, email: str) -> str:
    """
    Send an email using Gmail SMTP server.

    Args:
        subject (str): Email subject
        body (str): Email body in markdown format
        email (str): Recipient email address

    Returns:
        str: Message ID of the sent email
    """
    html_body = markdown_to_html(body)

    # Create message
    msg = MIMEMultipart()
    msg['From'] = GMAIL
    msg['To'] = email
    msg['Subject'] = subject

    # Attach HTML content
    msg.attach(MIMEText(html_body, 'html'))

    try:
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable TLS

        # Login to Gmail
        server.login(GMAIL, GMAIL_APP_PASSWORD)

        # Send email
        server.send_message(msg)

        # Close the connection
        server.quit()

        return f"Email Sent successfully to {email}"
    except Exception as e:
        raise Exception(f"Failed to send email via Gmail: {str(e)}")


def send_report_via_email(
        subject: str,
        body: str,
        email_address: str) -> str:
    """
    Use this tool to send the generated report.

    Args:
        subject (Annotated[str, &quot;Email subject of report for email sending&quot;]): _description_
        body (Annotated[str, &quot;Report content in markdown from reporting agent for email sending&quot;]):

    Returns:
        str: description
    """
    bod_in_html = markdown_to_html(body)
    result = send_email_gmail(subject, bod_in_html, email_address)
    return result


if __name__ == "__main__":
    subject = "Testing"
    body = ""
    email = "nelsonlin0321@gmail.com"
    send_email_gmail(subject=subject, body=body, email=email)
    # python -m src.utils_email
