from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Your Auth Token from twilio.com/console
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

to_whatsapp_number =   os.environ['TO_WHATSAPP_NUMBER'] 
from_whatsapp_number = os.environ['FROM_WHATSAPP_NUMBER'] 

client.messages.create(
    body='Ahoy world!',
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)