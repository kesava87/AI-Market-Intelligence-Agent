import smtplib
from email.message import EmailMessage
from pathlib import Path

from config import (
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER,
)


def send_email():
    report_path = Path("reports/output/ai_market_report.html")

    if not report_path.exists():
        print("❌ Report not found:", report_path)
        return

    msg = EmailMessage()

    msg["Subject"] = "📈 Daily AI Market Intelligence Report"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    msg.set_content(
        "Hello,\n\nYour AI Market Intelligence Report has been generated successfully.\n\nThe HTML report is attached.\n\nRegards,\nAI Market Intelligence Agent"
    )

    with open(report_path, "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype="text",
            subtype="html",
            filename="AI_Market_Report.html",
        )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("✅ Email sent successfully!")