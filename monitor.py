import requests
import hashlib
import json
import os
import notify

URL = "https://alpha123.uk/zh/"
STATE_FILE = "state.json"


def get_content():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(URL, headers=headers, timeout=10)
    return r.text


def get_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def load_old():
    if not os.path.exists(STATE_FILE):
        return None
    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_new(hash_value):
    with open(STATE_FILE, "w") as f:
        json.dump({"hash": hash_value}, f)


def main():
    print("=== monitor start ===")

    content = get_content()
    new_hash = get_hash(content)

    old = load_old()

    if old is None:
        print("first run, save state only")
        save_new(new_hash)
        return

    if old["hash"] != new_hash:
        print("CHANGE DETECTED!")

        notify.send_push(
            "Alpha123 空投更新",
            "检测到页面内容变化，请立即查看：https://alpha123.uk/zh/"
        )

        save_new(new_hash)
    else:
        print("no change")


if __name__ == "__main__":
    main()
