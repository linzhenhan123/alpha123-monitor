import requests
import hashlib
import json
import os
from notify import push
from config import URL

DATA_FILE = "data.json"


def get_html():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers, timeout=20)
    return r.text


def load_old():
    if not os.path.exists(DATA_FILE):
        return ""
    with open(DATA_FILE, "r") as f:
        return json.load(f).get("md5", "")


def save(md5):
    with open(DATA_FILE, "w") as f:
        json.dump({"md5": md5}, f)


def main():
    html = get_html()
    md5 = hashlib.md5(html.encode()).hexdigest()

    old_md5 = load_old()

    if old_md5 == "":
        save(md5)
        print("初始化完成")
        return

    if md5 != old_md5:
        save(md5)
        push(
            "🆕 Alpha123 空投更新",
            f"检测到页面变化\n\n👉 {URL}"
        )
        print("发现更新，已推送")
    else:
        print("无变化")


if __name__ == "__main__":
    main()
