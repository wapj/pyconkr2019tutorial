# type으로 클래스를 만들어보자
Kakao = type("Kakao", (), {"location": "pangyo", "member_cnt": 3000})

print(Kakao)  # class
print(Kakao())  # object
print(Kakao.location)
print(Kakao.member_cnt)

# 부모클래스도 넣어보자
KakaoPage = type(
    "KakaoPage", (Kakao,), {"service_name": "kakaopage", "member_cnt": 200}
)
print(KakaoPage)
print(KakaoPage())
print(KakaoPage.member_cnt)


def where(self):
    return self.location


KakaoPay = type("KakaoPage", (Kakao,), {"service_name": "kakaopay", "where": where})

print(hasattr(Kakao, "location"))  # true
print(hasattr(KakaoPay, "location"))  # true
pay = KakaoPay()
print(pay.where())


# 동적으로 함수를 추가 할 수도 있어요.
def what_service(self):
    return "bank_service"


KakaoPay.what_service = what_service
print(hasattr(KakaoPay, "what_service"))  # true
