def main():
    print("=== monitor start ===")

    content = get_content()
    new_hash = get_hash(content)

    old = load_old()

    # ❗关键修复：第一次也发测试通知（确认链路）
    if old is None:
        print("first run -> send test push")

        notify.send_push(
            "Alpha123监控启动成功",
            "系统已正常运行，将开始监控空投变化"
        )

        save_new(new_hash)
        return

    if old["hash"] != new_hash:
        print("CHANGE DETECTED!")

        notify.send_push(
            "Alpha123 空投更新",
            "检测到页面变化：https://alpha123.uk/zh/"
        )

        save_new(new_hash)
    else:
        print("no change")
