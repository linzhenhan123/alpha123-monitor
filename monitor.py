import requests
import hashlib
import notify
import os

URL = "https://alpha123.uk/zh/"
STATE_FILE = "/tmp/state.txt"

def get_content():
    r = requests.get(URL, timeout=10)
    return r.text

def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def main():
    print("=== monitor start ===")

    content = get_content()
    new_hash = get_hash(content)

    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            old_hash = f.read().strip()
    else:
        old_hash = ""

    if old_hash == "":
        print("first run")
        with open(STATE_FILE, "w") as f:
            f.write(new_hash)
        return

    if new_hash != old_hash:
        notify.send_push(
            "Alpha123更新",
            "检测到页面变化：https://alpha123.uk/zh/"
        )
        with open(STATE_FILE, "w") as f:
            f.write(new_hash)
    else:
        print("no change")

if __name__ == "__main__":
    main()
