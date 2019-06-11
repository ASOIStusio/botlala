#/url {ссылка на профиль инсты} – начать следить за этим аккаунтом

#INSERT INTO dbo.listt (id,name,track,chat_id,status) VALUES  (6 , 'lena','instlena',1325,0); вставка в бд
#/del { ссылка на профиль инсты } – не отслеживать этого пользователя
#UPDATE listt SET track='' WHERE track='inslexa'; - поле track заменить на пустое значение 
#/list – список отслеживаемых аккаунтов 
# select track from listt where name='lena'
#/vip – плюшки вип аккаунта

import platform
import token_id
import re
token = token_id.token
print(token)


# import bd
#https://www.instagram.com/molodoy_tryp/

def strcheck(text): #чистит стоку от пробелов и в text записыпается только краткую ссылку
    text = re.sub(r'\s+', ' ', text) #удаление лишних пробелов 
    text = text.replace('https://www.instagram.com/','')
    text = text.replace('/','')
    text = text.strip(' ')#удаление пробелов в начале и конце строки
    return text[4:]




    
def main():
    URL = 'https://api.telegram.org/bot' + token+'/'
    track=['molodoy_tryp','']
    print (type(track))
    track=['molodoy_tryp','tryp']
    print("Бот запущен")
    while True:
        text = input('Ожидание ввода команды \n')
        vip=1
        if text=='/stop':
            break
        if '/url ' in text:
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
        if '/del' in text:
            print('Прекращение слежки')
            print("Вы следите за:")
            while True:
                for item in track:
                    print(track.index(item)+1,'- чтобы не следить за',item)
                ans = input (str(len(track)+1)+' - Назад \n')
                ans = int(ans)-1 #ибо нумерация с 0
                try:
                    print('Вы больше не следите за '+track[ans])
                    del track[ans]
                    break
                    #UPDATE listt SET track='' WHERE track='inslexa';
                except IndexError:
                    if ans==len(track): #выход из цикла (назад)
                        break
                    print('Ошибка ввода числа')
            break
        if '/list' in text:
            print("Вы следите за:")
            for item in track:
                print(track.index(item)+1,'- ',item)
        if '/vip' in text:
            print("Для получения Vip пишите в нашу группу в вк /{ссылка}/")
    print (track)
    print("Бот остановлен")

if __name__ == '__main__':
    main()


# def com_list(conn,name):
#     print("список отслеживаемых аккаунтов")
#     cursor = conn.cursor()
#     cursor.execute("select track,name,chat_id from dbo.listt WHERE name ='"+name+"' ")
#     for row in cursor:
#         print(f'row = {row}')
#     print()