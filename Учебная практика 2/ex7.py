
# Написать простой парсер для сайта rksi.ru/schedule который выводит пары 
# на сегодняшний день в формате: {название предмета} - {кабинет} - {преподаватель}

from pprint import pprint
import requests, bs4, re

group = 'ПОКС-44b'
url = 'https://rksi.ru/schedule'
config = {
    'data': {
        'group': group.encode('windows-1251'),
        'stt': 'Показать!'.encode('windows-1251')
    },
    'headers': {
        'accept-enconding': 'gzip, deflate, br',
        'content-type': 'application/x-www-form-urlencoded',
        'connection': 'keep-alive',
    }
}
response = requests.post(url, data=config['data'], timeout=5)
response.encoding = 'windows-1251'
soup = bs4.BeautifulSoup(response.text, 'html.parser')
schedule_raw = soup.find_all('form')[-1].find_next_siblings()
schedule_raw = ''.join([str(tag)
                        for tag in schedule_raw[1:]]).split('<hr/>')[:-1]

# <p>09:40  —  11:10<br/><b>УП</b><br/>Бельчич Д.С., ауд. 303-1</p>
regexp = r"<p>(\d\d:\d\d\s+—\s+\d\d:\d\d)<br\/><b>(.+?)<\/b><br\/>(.+?)<\/p>"
pprint(re.findall(regexp, schedule_raw[0]))
