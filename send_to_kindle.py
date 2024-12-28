import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
from dotenv import load_dotenv
import logging
import sys
from pathlib import Path

# Load environment variables
load_dotenv()

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    ),
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


def send_email(file_path: str) -> bool:
    """
    Sends an email with the provided PDF file as attachment.

    Args:
        file_path (str): Path to the PDF file to be sent.

    Returns:
        bool: True if email was sent successfully, False otherwise.
    """
    try:
        # Validate file exists and is PDF
        file_path = Path(file_path)
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            return False
        if file_path.suffix.lower() != ".pdf":
            logger.error(f"File is not a PDF: {file_path}")
            return False

        # Get email configuration from environment variables
        sender_email = os.environ.get("SENDER_EMAIL")
        recipient_email = os.environ.get("RECIPIENT_EMAIL")
        smtp_server = os.environ.get("SMTP_SERVER", "in-v3.mailjet.com")
        smtp_port = int(os.environ.get("SMTP_PORT", "587"))

        if not all([sender_email, recipient_email]):
            logger.error(
                "Missing email configuration in environment variables"
            )
            return False

        msg = MIMEMultipart()
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        msg["Subject"] = f"[PDF] {current_time}"
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg.attach(MIMEText("PDF document attached"))

        # Attach PDF file
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "pdf")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={file_path.name}",
            )
            msg.attach(part)

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(
                os.environ.get("MAILJET_USERNAME"),
                os.environ.get("MAILJET_PASSWORD")
            )
            smtp.send_message(msg)
            logger.info(
                f"Email sent successfully with attachment: {file_path.name}"
            )
            return True

    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}", exc_info=True)
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python send_email.py <pdf_file>")
        sys.exit(1)

    success = send_email(sys.argv[1])
    sys.exit(0 if success else 1)
