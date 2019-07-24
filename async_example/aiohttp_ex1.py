# 파이썬에서 기본으로 제공해주는 asyncio 라이브러리는 http 프로토콜을 지원하지 않습니다.
# aiohttp 라는 서드파티 라이브러리를 사용해야해요~
# 아래의 명령어로 설치후 진행합시다.
# pip3 install aiohttp
# 이번에는 파일을 하나 다운로드 받아보는 것을 해볼거예요.
# http://pycon.gyus.me/test.txt  파일을 받아봅시다.

import asyncio
import aiohttp


async def aioget(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            return await res.text()


BASE_URL = "http://dev.gyus.me/"


async def main():
    result = await aioget(BASE_URL + "test.txt")
    print(result)


asyncio.run(main())
