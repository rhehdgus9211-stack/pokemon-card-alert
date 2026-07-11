def check_product(name, url):
    try:
        r = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        text = r.text
        print(text[:2000])

        # 구매불가가 없으면 상태 확인 알림
        if "구매불가" not in text:
            send_push(name, url)

    except Exception as e:
        print(name, e)
