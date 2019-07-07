import ssl

import certifi
import slack
OAUTH_ACCESS_TOKEN='xoxp-686051350340-688371555767-686935360773-7b5bad0b8584df9b9da16923383bdffd'
BOT_ACCESS_TOKEN='xoxb-686051350340-688566757703-wCpF7x4DsKHsVZlgDPqvsu3l'



TOKEN = 'xoxb-686051350340-686055790884-agXhuReNc1AF12pijXY85LTQ'
def main():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    rtm_client = slack.RTMClient(token=BOT_ACCESS_TOKEN, ssl=ssl_context)
    print("andybot START!")
    res = rtm_client.start()
    print(res)



@slack.RTMClient.run_on(event="message")
def control_message(**payload):
    """
    봇에 명령을 내리기 위한 첫번째 진입점이다.
    :param payload:
    :return:
    """
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
            # text=f"<@{user}> : {text}",
            text=f"{text}",
            thread_ts=thread_ts
        )



if __name__ == '__main__':
    main()