from twilio.rest import Client
import  smtplib
TWILIO_SID = "id"
TWILIO_AUTH_TOKEN = "Token"
TWILIO_VIRTUAL_NUMBER = "+from number"
TWILIO_VERIFIED_NUMBER = "+91 to number"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login("wefg@gmail.com", "34rt3rtgh")
            for email in emails:
                connection.sendmail(
                    from_addr="wefg@gmail.com",
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
