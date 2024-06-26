from twilio.rest import Client
import os

TWILIO_SID = "ACb65f258128faaea33e133366265f11a4"
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_VIRTUAL_NUMBER = "+12055493689"
TWILIO_VERIFIED_NUMBER = os.environ['TWILIO_VERIFIED_NUMBER']


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
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
