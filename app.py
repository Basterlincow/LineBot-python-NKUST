from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('vF5ttR4VfzPsvyWeIDiaZzq0rtMBJdIF8nSyk+Xme1d5NRAL28/kXw+vpwQR1Q+J1CGg9KtsYjeT+TC5V3CCfeasOSG1W0OkYKoO9rKAsTyQZH+6gikAUiSn3YhjW8VNwGDFCN/q6cHIHaqym3qGcwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('d211ec85f8fa5a05077544b6a6367c49')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    text = event.message.text
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        if text == 'test':
            text='success'
        else
            text=text    

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
