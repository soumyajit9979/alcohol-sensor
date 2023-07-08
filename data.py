import serial
import requests
from twilio.rest import Client
import json
from urllib.request import urlopen


account_sid = "AC6b4eb901e1a001899b26646910090c57"
auth_token = "49b5d0b451950d936e4dbb2341cf7360"
twilio_number = "+14846421339"
recipient_number = "+919429756022"

serial_port = "COM12"  # Update with your serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

api_key = "8OERWHRMPKTWQLHL"  # Replace with your ThingSpeak API key
url = f"https://api.thingspeak.com/update.json"
count = 0
# d = 0

client = Client(account_sid, auth_token)
while True:
    line = ser.readline().decode().strip()
    # d = int(line)
    # print(line)
    # print("hello")
    # print(line)
    if line == "":
        line = 0

    elif line != "":
        line = int(line)

    print(line)

    count = count + 1
    if count == 70:
        payload = {"api_key": api_key, "field1": line}
        response = requests.get(url, params=payload)
        count = 0

    elif int(line) > 300:
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)
        x = f'driver is drunk at city: {data["city"]}, region: {data["region"]}, country: {data["country"]}, Lat & Long: {data["loc"]}'
        # Send the message via Twilio
        message = client.messages.create(
            body=x, from_=twilio_number, to=recipient_number
        )
        print("Message sent successfully!")

# Close the serial port
ser.close()
