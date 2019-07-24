# run도 원래 파이썬에 있는걸 가져다 써볼게요.
import asyncio


async def greeting(name):
    return "hello " + name


async def main():
    result = await greeting("pyconkr 2019")
    print(result)


asyncio.run(main())

# output
# hello pyconkr 2019
