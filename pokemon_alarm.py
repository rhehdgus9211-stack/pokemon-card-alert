import requests

NTFY_TOPIC = "pokemon-card-alert-7x39kq82"

PRODUCTS = {
    "151": "https://m.pokemonstore.co.kr/pages/product/product-detail.html?productNo=114169373",
    "테라스탈": "https://m.pokemonstore.co.kr/pages/product/product-detail.html?productNo=124381031",
    "샤트": "https://m.pokemonstore.co.kr/pages/product/product-detail.html?productNo=116178963",
    "이브이": "https://m.pokemonstore.co.kr/pages/product/product-detail.html?productNo=114165789",
    "V스타": "https://m.pokemonstore.co.kr/pages/product/product-detail.html?productNo=114167543",
}


def send_push(name, url):
    requests.post(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=f"Pokemon card test\n{name}\n{url}",
        headers={
            "Title": "Pokemon Card Alert",
            "Priority": "high"
        }
    )


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

        # 테스트용 무조건 알림
        send_push(name, url)

    except Exception as e:
        print(name, e)


for name, url in PRODUCTS.items():
    check_product(name, url)
