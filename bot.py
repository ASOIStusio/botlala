import requests
import token_id
import random
from yo import get_btc
import json
import bd
from time import sleep
token = token_id.token
print(token)
URL = 'https://api.telegram.org/bot' + token+'/'
print(URL)
# https://api.telegram.org/bot715015872:AAF-_GzjPvxOqmTiDh4ynbEkdgPJdkmOHrw/sendmessage?chat_id=524698524&text=hi


track_users='sanya, '
global i
i=1
global last_update_id
last_update_id = 0

def get_updates():
    url = URL+'getupdates'
    global i
    print("Обновление сообщений №",i)
    i+=1

    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id= last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        print(chat_id)
        message_text = last_object['message']['text']
        print(message_text)
        message = {'chat_id': chat_id,
                'text': message_text}
        return message
    return None


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def stop():#-----------------------------------------------------
        sleeep=random.randint(10, 15)
        print('Задержка между запросами:{} (c.)'.format(sleeep))
        sleep(sleeep)

def main():
    print("Бот запущен")
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            if text=='!btc':
                send_message(chat_id, get_btc())
            if text=='!stop':
                break
            if '!url ' in text:
                send_message(chat_id, 'Теперь вы будете получать все посты и истории этого профиля')
            if '!del ' in text:
                print('Выбирете ')
            stop()
        print('Обновлений нет')
        if i==3:
            break
        stop()


if __name__ == '__main__':
    main()
