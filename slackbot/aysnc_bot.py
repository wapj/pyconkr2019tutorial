import asyncio
import os
import slack

client = slack.WebClient(token=os.environ["BOT_ACCESS_TOKEN"], run_async=True)


async def send_async_message(channel="#random", text="Hello"):
    response = await client.chat_postMessage(channel=channel, text=text)
    assert response["ok"]


async def main():
    await send_async_message()


asyncio.run(main())
