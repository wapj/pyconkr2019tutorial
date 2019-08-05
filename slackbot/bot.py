import os
import random
import ssl
import time
from functools import wraps

import aiohttp
import certifi
import requests
import slack
from bs4 import BeautifulSoup


def main():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    rtm_client = slack.RTMClient(token=os.environ["BOT_ACCESS_TOKEN"], ssl=ssl_context)
    print("bot START!")
    print(register)
    res = rtm_client.start()
    print(res)


register = {}


def command(cmd):
    def deco(func):
        register[cmd] = func

        @wraps(func)
        def wraped(*args, **kwargs):
            print(args)
            return func(*args, **kwargs)

        return wraped

    return deco


async def send(client, data, text):
    channel_id = data.get("channel")
    # await 가 있는 버전과 없는 버전 비교해보기
    # client.chat_postMessage(channel=channel_id, text=text)
    await client.chat_postMessage(channel=channel_id, text=text)


async def download_img(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            if res.status == 200:
                print(res.text)


@command("아재개그")
async def azae_gag(client, data):
    """아재개그를 보여줍니다."""

    await send(client, data, "길을 가다 나무를 주웠다를 3글자로?")
    await send(client, data, text="3")
    await send(client, data, text="2")
    await send(client, data, text="1")
    await send(client, data, text="정답 : 우드득")


@command("짤")
async def zzal(client, data):
    """구글에서 짤을 검색해서 보여줍니다. aiohttp를 사용합니다."""
    channel_id = data.get("channel")
    text = data.get("text")
    search = text[3:]

    # 구글은 이미지가 너무 작게나옴
    url = f"https://www.google.com/search?q={search}safe=off&tbm=isch&source=lnt&tbs=isz:l&sa=Xbiw=1280"

    # 네이버는 좀 크게나옴
    url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={search}"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")
    imgs = []

    for img in soup.find_all("img"):
        if img.get("data-source"):
            imgs.append(img.get("data-source") + "&tm=" + str(int(time.time())))

    # 한장만 뽑기
    send(client, data, str(random.choice(imgs)))


@command("메아리")
async def echo(client, data):
    """에코가 돌아옵니다."""
    send(client, data, data.get("text"))


@command("help")
async def help(client, data):
    """님이 실행하신 그것입니다. """
    help_txt = ""
    for key, func in register.items():
        # if key != "help":
        desc = func.__doc__ if func.__doc__ else ""
        help_txt += f"{key} : {desc}\n"

    client.chat_postMessage(channel=data.get("channel"), text=str(help_txt))


@slack.RTMClient.run_on(event="message")
async def control_message(**payload):
    """
    봇에 명령을 내리기 위한 첫번째 진입점이다.
    :param payload:
    :return:
    """

    data = payload["data"]
    print("===================================")
    print(data)
    print("===================================")
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user = data.get("user")
    text = data.get("text")
    thread_ts = data.get("ts")

    if user and text and text.startswith("!"):

        txt = text[1:]
        cmd = txt.split(" ")[0]
        func = register.get(cmd)
        if func:
            await func(web_client, data)

    # if user:
    #     res = web_client.chat_postMessage(
    #         channel=channel_id,
    #         # text=f"<@{user}> : {text}",
    #         text=f"{text}",
    #         thread_ts=thread_ts,
    #     )


if __name__ == "__main__":
    main()


# !대여, !반납 을 인식하도록 하게 해서 어떤 유저가 어떤 책을 빌리고 반납했는지, 확인할 수 있는 슬랙봇을 만들어보자.
# DB는 기본적으로는 필요없지만, 파일에는 json 형식으로 써서 import/export 가 가능하도록 해보자.
# !대여중 을 실행하면 현재 대여중인 책들이 누구에게 있는지 확인할 수 있도록 만들어 보자.
