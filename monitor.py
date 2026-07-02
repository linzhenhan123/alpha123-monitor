import notify

def main():
    print("=== monitor start ===")

    notify.send_push(
        "Alpha123测试通知",
        "如果你收到说明PushPlus正常"
    )

    print("END")

if __name__ == "__main__":
    main()
