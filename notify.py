import requests
from config import PUSHPLUS_TOKEN

def push(title, content):
    requests.post(
        "http://www.pushplus.plus/send",
        json={
            "token": PUSHPLUS_TOKEN,
            "title": title,
            "content": content
        },
        timeout=10
    )
