# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC0aa3e8a0c53e6b11253ae1a2a2e03440"
auth_token = "28e92f4fdce245de5088ede02ea55e43"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+919924191992", from_="+12768074146",
                                     body="Hello there! teri maaka saakinaka")
