from twilio.rest import Client

account="AC7b3bc85fc64d2fab72ada7e661e53a0e"
token="da3d677bce4738f64521a56d717737d3"
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(account,token)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'

# this is the number which will receive the message on whatsapp
to_whatsapp_number='whatsapp:+918217861039'

# function that sends a message to the number

def send_message(message):
    client.messages.create(body=message,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)
