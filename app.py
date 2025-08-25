import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("OPENWEATHER_API_KEY")
LINE_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
USER_ID = "Ud411a376c81141bb12e259d1a0ad08f1"

CITY = "Tokyo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&lang=ja&units=metric"

respons = requests.get(URL)
data = respons.json()

weather = data["weather"][0]["main"]
if weather == "Rain":
    message = "今日は雨です☔️"
else:
    message = "今日は雨ではありません😆"


def send_line_message(message: str):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    body = {
        "to":USER_ID,
        "messages":[{"type":"text", "text":message}]
    }
    response = requests.post(url, headers=headers, json=body)
    print("LINE送信結果:", response.status_code, response.text)

send_line_message(message)