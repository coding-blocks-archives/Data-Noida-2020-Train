from flask import Flask, request

import requests

app = Flask("hello")

token = "1234567890"


def bot(recipient, text):
    url = r"https://graph.facebook.com/v6.0/me/messages?access_token=EAALVdIQvwBcBAJMuUTf6a2Lojr6MqsGWaf5AmIt5jb63DgGmA6omnx8G92rGQ5eJlZCVGfTAHof0q4IsGH6VlRDtqhyX489IRnZBSN5IWCaatPu6ZCCtETE9Hp5DMggFInWW5Rlr1crpNVJc7HZCEbBIbj1Je5D08XF8z7JiAAZDZD"

    d1 = {
        "recipient": {
            "id": recipient
        },
        "message": {
            "text": "bot says " + text
        }
    }

    requests.post(url, json=d1)


@app.route("/check/", methods=["GET"])
def sayhi():
    return "working"


@app.route("/callback/", methods=["GET"])
def get_callback():
    if token == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return "not working"


@app.route("/callback/", methods=["POST"])
def post_callback():
    output = request.get_json()

    for entry in output.get("entry"):
        if "messaging" in entry:
            for messaging in entry.get("messaging"):
                sender = messaging.get("sender").get("id")
                recipient = messaging.get("recipient").get("id")

                text = "You sent an attachment"

                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")

                print(sender, recipient, text)
                bot(sender, text)

    return "done"

app.run()