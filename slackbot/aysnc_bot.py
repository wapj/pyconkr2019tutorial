import ssl
import certifi

### 토큰은 슬랙과 통신을 하기위해 필요하므로 잘 저장해두자.
import slack


def main():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    slack_token = BOT_OAUTH_ACCESS_TOKEN
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()



