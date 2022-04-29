from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


from message import *

import tempfile, os
import datetime
import time

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

line_bot_api = LineBotApi('W8dKGNPC0AbNOg9uVqEEF/+uMrOPXH6ZB+6/x8unW8d34WBxUKWqzYpXvLKiFzkUTQQIZg2eAQ7DhPRaRQk/orgxSL9LwGib6/9FBYhtG7TGaCaki6sAujJr0D05pBrE6/wNx1SodcP6yfku3c714wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c1f78c561375e97c4fab95fe07bdd150')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if 'CV' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'introduce' in str(msg).lower():
        message = introduce_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '梗圖' in msg:
        message = fun_image_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '你好' in msg or "hello" in str(msg).lower() or "hi" in str(msg).lower() or '嗨' in msg:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text="請輸入 'CV' 或 'introduce' 或 '梗圖'")
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
