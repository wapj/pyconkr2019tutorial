import ssl

import certifi
import slack



TOKEN = 'xoxb-686051350340-686055790884-agXhuReNc1AF12pijXY85LTQ'
def main():

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    rtm_client = slack.RTMClient(token=TOKEN, ssl=ssl_context)
    print("andybot START!")
    res = rtm_client.start()
    print(res)



@slack.RTMClient.run_on(event="message")
def message(**payload):
    data = payload["data"]
    print("===================================")
    print(data)
    print("===================================")
    web_client = payload['web_client']
    channel_id = data.get('channel')
    user = data.get('user')
    text = data.get('text')
    thread_ts = data.get('ts')

    if user:
        res = web_client.chat_postMessage(
            channel=channel_id,
            text=f"<@{user}> : {text}",
            thread_ts=thread_ts
        )



if __name__ == '__main__':
    main()