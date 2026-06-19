import smtplib

from email.message import EmailMessage


EMAIL = "janavijain0620@gmail.com"

PASSWORD = "seems_goodnow"


def send_email(

    receiver,

    subject,

    body

):

    try:

        msg = EmailMessage()

        msg["Subject"] = subject

        msg["From"] = EMAIL

        msg["To"] = receiver

        msg.set_content(body)

        with smtplib.SMTP_SSL(

            "smtp.gmail.com",

            465

        ) as smtp:

            smtp.login(

                EMAIL,

                PASSWORD

            )

            smtp.send_message(msg)

        return "Email sent successfully."

    except Exception:

        return "Unable to send email."