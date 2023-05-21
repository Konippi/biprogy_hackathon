import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()
ACCESS_TOKEN = os.environ.get("LINE_BOT_ACCESS_TOKEN")
API_URL = os.environ.get("LINE_BOT_API_URL")


def send_coupon(message):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {ACCESS_TOKEN}"}
    body = {
        "messages": [
            {"type": "text", "text": message},
            {"type": "sticker", "packageId": "8515", "stickerId": "16581246"},
        ]
    }
    requests.post(url=API_URL, headers=headers, data=json.dumps(body))
