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

        print(name, "페이지 확인")
        print("구매불가 포함:", "구매불가" in text)
        print("품절 포함:", "품절" in text)

        if "구매불가" not in text:
            send_push(name, url)

    except Exception as e:
        print(name, e)
