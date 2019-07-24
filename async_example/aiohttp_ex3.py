# future 의 iterator 를 리턴하는 as_completed 를 사용해도 좋습니다.
import asyncio
import aiohttp


async def aioget(url, is_binary=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if is_binary:
                return await res.read()
            return await res.text("UTF-8")


BASE_URL = "http://dev.gyus.me/"


async def download_one(url, filename):
    print(url, filename)
    img = await aioget(url, True)
    with open(f"./tmp/{filename}", "wb") as f:
        f.write(img)


async def main():
    tasks = [download_one(f"{BASE_URL}{i}.png", f"{i}.png") for i in range(1, 13)]
    for future in asyncio.as_completed(tasks):
        await future


asyncio.run(main())
