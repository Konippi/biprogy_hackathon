import os
import requests
import json


ACCESS_TOKEN = os.environ['LINE_BOT_ACCESS_TOKEN']
API_URL = os.environ['LINE_BOT_API_URL']


def send_ticket(message):
    url = ''
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer{{{ACCESS_TOKEN}}}'
    }
    body = {
        'messages': [
            {
                'type': 'text',
                'text': message
            }
        ]
    }
    requests.post(url=url, headers=headers, data=json.dumps(body))
