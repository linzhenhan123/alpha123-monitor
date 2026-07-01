import requests

TOKEN = "fcec3a64057e452cb144899f827b5c33"

def send_push(title, content):
    url = "http://www.pushplus.plus/send"

    data = {
        "token": TOKEN,
        "title": title,
        "content": content,
        "template": "txt"
    }

    try:
        r = requests.post(url, json=data, timeout=10)
        print("Push status:", r.status_code)
        print("Push response:", r.text)
    except Exception as e:
        print("Push error:", str(e))
