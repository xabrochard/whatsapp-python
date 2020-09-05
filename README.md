# Testing the Twilio API for WhatsApp
A Python application to send and receive messages with WhatsApp using the Twilio API for WhatsApp.

# Getting started 
Follow the guide here:
https://www.twilio.com/docs/whatsapp/quickstart/python

# Setting up the application
Add your credentials and To/From phone numbers as environment variables in a `twilio.env` file and source them:
```
echo "export TWILIO_ACCOUNT_SID='ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'" > twilio.env
echo "export TWILIO_AUTH_TOKEN='your_auth_token'" >> twilio.env
echo "export TO_WHATSAPP_NUMBER='to_whatsapp_number'" >> twilio.env
echo "export FROM_WHATSAPP_NUMBER='from_whatsapp_number'" >> twilio.env
source ./twilio.env
```
Make sure that Git ignores the `twilio.env` file:
```
echo "twilio.env" >> .gitignore
```
More info [here](https://www.twilio.com/docs/usage/secure-credentials).

