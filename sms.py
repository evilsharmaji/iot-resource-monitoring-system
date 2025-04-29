from twilio.rest import Client

def send_alert(msg):
    account_sid = 'Evil_AI'
    auth_token = '34AMY610'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=msg,
        from_='+1234567890',  # Your Twilio number
        to='+0987654321'      # Your phone number
    )

# Example usage
send_alert("Anomaly Detected: Sudden spike in water usage!")
