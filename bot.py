import requests
import token_id
import random
import urllib
from yo import get_btc
import json
import re
#import bd
from time import sleep
import urllib.request
token = token_id.token
URL = 'https://api.telegram.org/bot' + token+'/'
print(URL)
# https://api.telegram.org/bot715015872:AAF-_GzjPvxOqmTiDh4ynbEkdgPJdkmOHrw/sendmessage?chat_id=524698524&text=hi

# https://www.instagram.com/p/Bx91l8mBVT-/

track_users='sanya, '
global i
i=1
global last_update_id
last_update_id = 0

# функция скачивания историй
def get_history(link_to_history):
    link_to_history = link_to_history.replace(link_to_history[-1],'')
    print('Начинаем закачку видео... ',link_to_history)
    #Получаем ответ страницы и выводим исходный код страницы
    response = requests.get(link_to_history)
    name_video = 'video.mp4'

    text_for_parser = response.content
    text_for_parser = str(text_for_parser)

    result = re.findall(r'http.*\.mp4.*"', text_for_parser)

    print('Начинаем закачку видео... ')
    request.urlretrieve(result[0], name_video)
    print('Видео загружено')

# функция проверки сообщений
def get_updates():
    url = URL+'getupdates'
    global i
    print("Обновление сообщений №",i)
    i+=1
    r = requests.get(url)
    return r.json()
#https://api.telegram.org/bot715015872:AAF-_GzjPvxOqmTiDh4ynbEkdgPJdkmOHrw/sendPhoto?chat_id=524698524&photo=https:/
def send_photo(chat_id, text):
    

    url = URL + 'sendPhoto?chat_id={}&photo={}'.format(chat_id, text)
    print ()
    requests.get(url)


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id= last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        print('Сообщение - '+message_text)
        message = {'chat_id': chat_id,
                'text': message_text}
        return message
    return None

def strcheck(text): #чистит стоку от пробелов и в text записыпается только краткую ссылку
    text = re.sub(r'\s+', ' ', text) #удаление лишних пробелов 
    text = text.replace('https://www.instagram.com/','')
    text = text.replace('/','')
    text = text.strip(' ')#удаление пробелов в начале и конце строки
    return text[4:]

def send_message(chat_id,text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def stop():#-----------------------------------------------------
        sleeep=10
        print('Задержка между запросами:{} (c.)'.format(sleeep))
        sleep(sleeep)



def main():
    # некий аналог БД
    # таблица где хранится имена юзеров, количество отслеживаемых юзеров, статусы
    #   Id| Name_user   | kol-vo_Track_user | Chat_id |	Status	|
    bd_main = [
        [1,'Саня Санек' ,1                  , '11111' , 'free' ], 
        [2,'Вася вася'  ,2                  , '22222' , 'vip'  ]
    ]
    # хранится ссылки отслеживаемых аккаунтов и ссылки на их последние публикации
    #  id_account | id_user | track_account | Last_link_post | Last_link_history |
    bd_accounts = [
       [1         ,1        ,        'inst1',    'http/post1',    'http/history1'],
       [2         ,2        ,      'inst2_1',  'http/post2_1',  'http/history2_1'],
       [3         ,2        ,      'inst2_2',  'http/post2_2',  'http/history2_2'],
       [4         ,2        ,      'inst2_3',  'http/post2_3',  'http/history2_3']
    ]
    while True:
        answer = get_message()
        #/url
        #/del { ссылка на профиль инсты } – не отслеживать этого пользователя
        #/list – список отслеживаемых аккаунтов 
        #/vip – плюшки вип аккаунта
        
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            send_message(chat_id, 'Бот запущен')
            print('text',text)
            if text=='/stop':
                break
            if '/url ' in text:
                send_message(chat_id, 'Теперь вы будете получать все посты и истории этого профиля')
                text = strcheck(text)
                if text=="":
                    print("Вы ввели команду без ссылки")
                    break
                if text.count(' ', 0,) >= 2 and vip == 0: #если нашло 2 пробела, то введен не один аккаунт
                    print('Вы ввели больше одного аккаунта. Следить за несколкими аккаунтами можно в Vip версии')
                    break
                #INSERT INTO dbo.listt (id,name,track,chat_id,status) VALUES  (6 , 'lena','instlena',1325,0); вставка в бд
                x = text.split()
                for l in x:
                    if  track.count(l) == False:
                        #проверка на то существует ли аккаунт сюда тыкнуть нид
                        track = track + [l]
                        print("Записан аккаунт " + l)
                #следующие 3 строчки нид в функцию
                print("Вы следите за:") 
                for item in track:
                    print(track.index(item)+1,item)
                break
            if '/del ' in text:
                print('Выбирете ')
            if '/p' in text:
                # (id, '<a href="IMG_URL">&#8203;</a>',
                # parse_mode="HTML")
                text = text[3:]
                #send_message(chat_id,text)
                send_photo(chat_id,text)
                # url = URL +'sendPhoto'
                # files = {'photo': open('foto.jpg', 'rb')}
                # data = {'chat_id' : "111111111"}
                # r= requests.post(url, files=files, data=data)
                # print(r.json())
                # send_message(chat_id, 'https://www.instagram.com/p/BtBk9ibFtBj/media')
            if '/h' in text: #скачивает видео по ссылке 
                # удаляем слова команды из текста пользователя
                text = text[3:]
                #get_history(text)
                send_message(chat_id, text)
            if '/h' in text: #помощь по командам
                text = text[3:]
            stop()

        print('Обновлений нет')
        # if i==10:
        #     break
        stop()
    send_message(chat_id, 'Бот остановлен')


if __name__ == '__main__':
    print('Бот запущен')
    main()
