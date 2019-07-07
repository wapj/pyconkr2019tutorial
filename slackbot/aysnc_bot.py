import ssl
import certifi

### 토큰은 슬랙과 통신을 하기위해 필요하므로 잘 저장해두자.
import slack

OAUTH_ACCESS_TOKEN='xoxp-686051350340-688371555767-688566756855-b2e584dedd75b78b7f6425871e5f0302'
BOT_OAUTH_ACCESS_TOKEN='xoxp-686051350340-688371555767-688566756855-b2e584dedd75b78b7f6425871e5f0302'


def main():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    slack_token = BOT_OAUTH_ACCESS_TOKEN
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()



