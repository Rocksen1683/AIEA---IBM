from twilio.rest import Client

account="AC7b3bc85fc64d2fab72ada7e661e53a0e"
token="1977b6647dd3623bffd6b686631fce2e"
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
