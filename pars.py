import requests
from bs4 import BeautifulSoup
import re
from googletrans import Translator



class Pars:
    def __init__ (self, id):
        str1 = ''
        ### переводчик
        translator = Translator()
        #id1 = (translator.translate(id, src='ru', dest='en')).text
        ### переводчик

        # сайт картинок meme
        #url = "http://1001mem.ru/search?q=собака&p=1
        #id2 = random.randint(1, 2)
        #id2 = str(id2)
        url = 'https://yandex.ru/images/search?text=' + id + '%meme'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        #quo = soup.find_all('img', class_='attachment-thumbnail')
        quo = soup.find_all('div', class_=['serp-item', 'serp-item_type_search', 'serp-item_group_search'], limit=10)

        print(quo)

        chet = len(quo)
        #print(chet)

        if chet == 0:
            self.str1 = 'err'
        else:
            o = 0
            for i in quo:
                o = o + 1
                qul = re.search('(https.*?)"', str(i))

                # проверка ссылки
                al = 0
                try:
                    qul[1]
                except TypeError:
                    print('упс, что то не так =(')
                    al = 1
                if al == 0:
                    try:
                        print(qul[1])
                        check = requests.head(qul[1])
                        if check.status_code == 200:
                            if o != chet:
                                str1 = str1 + 'telebot.types.InputMediaPhoto("' + qul[1] + '"),'
                            else:
                                str1 = str1 + 'telebot.types.InputMediaPhoto("' + qul[1] + '")'

                        print(check.status_code)
                    except requests.exceptions.ConnectionError:
                        print('упс')
                    #print(qul[1])

                # проверка ссылки


            self.str1 = str1
            print(self.str1)
#Pars("dog")