import requests
import os 
from twilio.rest import Client

API_KEY =os.environ.get("API_KEY")
CNT = 4
parameters= {
    "lat" : -29.085215,
    "lon" : 26.159576,
    "appid" : API_KEY,
    "cnt" : CNT
}

account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_id = [weather_data['list'][i]['weather'][0]['id'] for i in range(CNT)]
for w_id in weather_id:
    if w_id <700:
        will_rain = True

if  will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☂",
        from_="whatsapp:+14155238886",
        to="whatsapp:+84818265472"
    )
    print(message.status)

