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
        data=f"Pokemon card available!\n{name}\n{url}",
        headers={
            "Title": "Pokemon Card Alert",
            "Priority": "high"
        },
        timeout=10
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

        has_unavailable = "구매불가" in text

        print(name, "확인")
        print("구매불가:", has_unavailable)

        # 구매불가가 없으면 구매 가능 상태로 판단
        if not has_unavailable:
            send_push(name, url)
            print("알림 전송:", name)
        else:
            print("재고 없음:", name)

    except Exception as e:
        print(name, "오류:", e)


for name, url in PRODUCTS.items():
    check_product(name, url)
