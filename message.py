from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def buttons_message():
    message = TemplateSendMessage(
        alt_text='下載袁紹奇的CV嗎??',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/ZjqTqn2.jpg",
            title="要不要下載CV阿?",
            text="點一下啦",
            actions=[
                URITemplateAction(
                    label="點擊下載我的履歷",
                    uri="https://www.cmlab.csie.ntu.edu.tw/~rickyyuan/CV/CV.pdf"
                )
            ]
        )
    )
    return message

# introduce
def introduce_message():
    message = TemplateSendMessage(
        alt_text='看一下其他連結',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/ZjqTqn2.jpg",
            title="這是一些關於我的連結",
            text="點擊下面連結了解更多",
            actions=[
                URITemplateAction(
                    label="Github",
                    uri="https://github.com/rickyyuan07"
                ),
                URITemplateAction(
                    label="Linkedin",
                    uri="https://www.linkedin.com/in/ricky-yuan-a1b540206/"
                ),
                URITemplateAction(
                    label="Facebook",
                    uri="https://www.facebook.com/rickyyuan07"
                )
            ]
        )
    )
    return message

# 梗圖
def fun_image_message():
    message = TemplateSendMessage(
        alt_text='給你看一堆梗圖 笑死',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/eai7KDx.png",
                    action=URITemplateAction(
                        label="梗圖1",
                        uri="https://www.facebook.com/ProgrammersCreateLife/photos/a.241809332534619/5014011645314340"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/udKGW0Q.png",
                    action=URITemplateAction(
                        label="梗圖2",
                        uri="https://www.facebook.com/ProgrammersCreateLife/photos/a.241809332534619/5013922188656619"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/LcvqXh6.png",
                    action=URITemplateAction(
                        label="梗圖3",
                        uri="https://www.facebook.com/ProgrammersCreateLife/photos/a.241809332534619/5013329505382554"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Mq4cari.png",
                    action=URITemplateAction(
                        label="梗圖4",
                        uri="https://www.facebook.com/ProgrammersCreateLife/photos/a.241809332534619/5013305205384984"
                    )
                )
            ]
        )
    )
    return message
