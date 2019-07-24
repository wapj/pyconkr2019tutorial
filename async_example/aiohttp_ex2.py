# 이번에는 여러개를 다운받는 것을 해보도록 합시다.
# tmp 라는 디렉토리를 만들고 그 디렉토리에 파일을 저장해 봅시다.
# 원래는 웹페이지를 파싱하는 내용이 있었지만, 생략했습니다.
# beautifulsoup 같은 라이브러리를 참고하세요~


import asyncio
import aiohttp


async def aioget(url, is_binary=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if is_binary:
                return await res.read()
            return await res.text("UTF-8")


BASE_URL = "http://dev.gyus.me/"


async def main():

    for i in range(1, 13):
        url = f"{BASE_URL}{i}.png"
        print(url)
        img = await aioget(url, True)
        with open(f"./tmp/{i}.png", "wb") as f:
            f.write(img)


asyncio.run(main())
