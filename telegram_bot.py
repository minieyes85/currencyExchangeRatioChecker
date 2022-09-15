import requests

# 텔레그램 개인 메시지 보내기
def tel_private_txt(message):
    headers = {'User-Agent':'Mozilla/5.0'}
    telegram_api_url = "https://api.telegram.org/bot"
    telegram_token = "2020360748:AAG480XZdsR27vUB_YFib-bMyN4P9KbUiXs"
    telegram_url = telegram_api_url + telegram_token + "/sendmessage"

    telegram_chat_id = "784833435" #개인
    # telegram_chat_id = "-645485749" #그룹
    response = requests.get(telegram_url, headers = headers, params={"chat_id" : telegram_chat_id , "text" : message})
    return response

# 텔레그램 그룹 메시지 보내기
def tel_group_txt(message):
    headers = {'User-Agent':'Mozilla/5.0'}
    telegram_api_url = "https://api.telegram.org/bot"
    telegram_token = "2020360748:AAG480XZdsR27vUB_YFib-bMyN4P9KbUiXs"
    telegram_url = telegram_api_url + telegram_token + "/sendmessage"

    # telegram_chat_id = "784833435" #개인
    telegram_chat_id = "-645485749" #그룹
    response = requests.get(telegram_url, headers = headers, params={"chat_id" : telegram_chat_id , "text" : message})
    return response