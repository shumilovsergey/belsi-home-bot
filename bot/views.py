from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from .serializers import telegram_format
from api.models import TelegramUsers
from server.const import BACK_BUTTON
from server.const import CLEAN_BUTTON


BOT_TOKEN = "7241522532:AAGRe5PqJziTmaphNVOooOIhYEvtAh_ADOI"
CHAT_ID = "507717647"
CAPTION = "Это то что вы выбрали!"
FILE_ID_1 = "AgACAgIAAxkBAAOsZ6VE8b0ZVQZP7mbFNYHwY6WLc_QAApTqMRtbMyhJv5-BcpymO5oBAAMCAANzAAM2BA"
FILE_ID_2 = "AgACAgIAAxkBAAOuZ6VFAwMEo8NQE-xvFiydeNyOfIUAApXqMRtbMyhJKzrBDTtn0zgBAAMCAANzAAM2BA"
FILE_ID_3 = "AgACAgIAAxkBAAOvZ6VFFu7CK-HIeuHf9tzAcCBSstkAApfqMRtbMyhJpWRCOthtKqQBAAMCAANzAAM2BA"


MAIN_MENU = {
    "inline_keyboard" :  [
        [
            {'text': 'Интерьерная мебель', 'callback_data': "1"}      
        ],
        [
            {'text': 'Детская мебель', 'callback_data': "2"}      
        ],
        [
            {'text': 'Школьная мебель', 'callback_data': "3"}      
        ],
        [
            {'text': 'Московская школа', 'callback_data': "4"}      
        ],
        [
            {'text': 'Обратная связь', 'callback_data': "5"}      
        ]
    ]
} 

QA_MENU ={
    "inline_keyboard" :  [
        [
            {'text': 'Сроки поставки', 'callback_data': "5-1"}      
        ],
        [
            {'text': 'Доставка', 'callback_data': "5-2"}      
        ],
        [
            {'text': 'Оплата', 'callback_data': "5-3"}      
        ],
        [
            {'text': 'Опросный лист', 'callback_data': "5-4"}      
        ],
        [
            {'text': '◀ назад', 'callback_data': "main_menu"}      
        ]
    ]  
}

QA_OR_MAIN = {
    "inline_keyboard" :  [
        [
            {'text': '◀ назад', 'callback_data': "5"},
            {'text': 'главное меню', 'callback_data': "main_menu"}       
        ]
    ]
}


@api_view(['POST'])
def getMessage(request):
    message = telegram_format(request.data)
    print(message)

    if message.text and "/start" in message.text:

        message.sendMessage(text="1. текст приветствия")
        message.sendMessage(text="Главное меню", keyboard=MAIN_MENU)

    if message.callback and message.callback=="main_menu":
        message.deleteMessage()
        message.sendMessage(text="Главное меню", keyboard=MAIN_MENU)
        
# main menu
    if message.callback and message.callback=="2":
        print("qq")

    if message.callback and message.callback=="3":
        print("qq")

    if message.callback and message.callback=="4":
        print("qq")

    if message.callback and message.callback=="5":
        message.deleteMessage()
        message.sendMessage(text="Текст для обратной связи\n и популярные вопросы", keyboard=QA_MENU)


# 1 Интерьерная мебель
    if message.callback and message.callback=="1":
        message.deleteMessage()
        message.sendMessage(
            text="категория интерьерная мебель",
            keyboard={
                "inline_keyboard" :  [
                    [
                        {'text': 'Кашпо', 'callback_data': "1-1"}      
                    ],
                    [
                        {'text': 'Шкафы', 'callback_data': "1-2"}      
                    ],
                    [
                        {'text': '◀ назад', 'callback_data': "main_menu"}
                    ]
                ] 
            })
    
    if message.callback and message.callback=="1-1":
        message.deleteMessage()
        message.sendMessage(
            text="категория интерьерная мебель",
            keyboard={
                "inline_keyboard" :  [
                    [
                        {'text': 'Black Moon напольное кашпо, S', 'callback_data': "1-1-1"}      
                    ],
                    [
                        {'text': 'Black Moon напольное кашпо, L', 'callback_data': "1-1-2"}      
                    ],
                    [
                        {'text': '◀ назад', 'callback_data': "1"}
                    ]
                ] 
            })
        
    if message.callback and message.callback=="1-1-1":
        message.deleteMessage()    
        media_send(chat_id=message.chat_id)
        message.sendMessage(
            text="можно заказать на нашем сайте",
            keyboard={
                "inline_keyboard" :  [
                    [
                        {'text': '◀ назад', 'callback_data': "1-1"},
                        {'text': 'Заказать', 'url': "https://belsi-home.ru/catalog/interernaya_mebel/kashpo/black_moon_napolnoe_kashpo_srednee/"}
                    ]
                ]
            }
        )
        
    

# 2 Детская мебель

# 3 Школьная мебель

# 4 Московская мебель

# 5 вопросы обратной связи
    if message.callback and message.callback=="5-1":
        message.deleteMessage()
        text = "ответ на вопрос - сроки доставки"
        message.sendMessage(text=text, keyboard=QA_OR_MAIN)

    if message.callback and message.callback=="5-2":
        message.deleteMessage()
        text = "ответ на вопрос - доставка"
        message.sendMessage(text=text, keyboard=QA_OR_MAIN)

    if message.callback and message.callback=="5-3":
        message.deleteMessage()
        text = "ответ на вопрос - оплата"
        message.sendMessage(text=text, keyboard=QA_OR_MAIN)

    if message.callback and message.callback=="5-4":
        message.deleteMessage()
        text = "ответ на вопрос - опросный лист"
        message.sendMessage(text=text, keyboard=QA_OR_MAIN)





        
    return Response("ok", status=200)





def hello(message):
    
    return



















def media_send(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMediaGroup"
    payload = {
        "chat_id": chat_id,
        "media": [
            {
                "type": "photo",
                "media": FILE_ID_1
            },
            {
                "type": "photo",
                "media": FILE_ID_2
            },
            {
                "type": "photo",
                "media": FILE_ID_3
            }
        ],
        "caption": "Фотографии товара"
    }

    # Send the request
    response = requests.post(url, json=payload)

    # Check the response
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.json())

    return

def start_2():
        # Prepare the payload for sendMessage
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text":  "Teкст приветсвия пользователя"
    }

    # Send the request
    response = requests.post(url, json=payload)

    # Check the response
    if response.status_code == 200:
        print("Text message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.json())

    return

def start():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "Тест для пользователя_3",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {"text": "Стол", "callback_data": "button1"}
                ],
                [
                    {"text": "Стул", "callback_data": "button2"}
                ],
                [
                    {"text": "Табуретка", "callback_data": "button3"}
                ],
                [{"text": "Елка", "callback_data": "button4"}]
            ]
        }
    }

    # Send the request
    response = requests.post(url, json=payload)

    # Check the response
    if response.status_code == 200:
        print("Text message with inline buttons sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.json())
    return