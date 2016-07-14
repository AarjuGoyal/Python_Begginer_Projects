from twilio.rest import TwilioRestClient
"""This file sends a message to the mobile nummber through twillio provided the twillio account details are correct"""
account_sid = "AC49a62eb0782850fa4c059f5fc6457dad" # Your Account SID from www.twilio.com/console
auth_token  = "aec277bb47870df01c9652871a50cfc6"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+919427627625",    # Replace with your phone number
    from_="+17474002882") # Replace with your Twilio number

print(message.sid)
