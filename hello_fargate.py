import requests


def send_slack_message():
    """ Send message to slack"""
    response = requests.post(
        "https://hooks.slack.com/services/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",
        json={
            "text": "Hello FOSS4G :smile:"
        },
    )

    print(response.status_code)


if __name__ == "__main__":
    print("Sending message")
    send_slack_message()
