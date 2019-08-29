import os

import requests

from dotenv import load_dotenv


def send_slack_message():
    """ Send message to slack"""
    web_hook = os.getenv("SLACK_WEB_HOOK", "NOT_SET")

    if web_hook == "NOT_SET":
        raise ValueError("Web Hook Env Var not set")

    response = requests.post(
        web_hook,
        json={
            "text": "Hello FOSS4G :smile:"
        },
    )

    print(response.status_code)


if __name__ == "__main__":
    load_dotenv()
    print("Sending message")
    send_slack_message()
