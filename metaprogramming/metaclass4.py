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
