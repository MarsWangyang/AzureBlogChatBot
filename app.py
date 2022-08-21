from flask import Flask
from linebot import LineBotApi
from linebot.models import TextSendMessage, FlexSendMessage
from linebot import LineBotApi
import os
import template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))


@app.route("/push-message")
def push_message():
    jsonFile = template.process_articles_template()
    if jsonFile['contents']['contents'] == []:
        line_bot_api.push_message(os.getenv('USER_ID'), TextSendMessage(text="No Articles Today. \n https://azure.microsoft.com/zh-tw/blog/"))
        return {"response":"info has been sent"}
    reply_message = [FlexSendMessage.new_from_json_dict(jsonFile)]
    line_bot_api.push_message(os.getenv('USER_ID'), reply_message)
    return {"response":"info has been sent"}


if __name__ == "__main__":
    app.run(debug=True)
    