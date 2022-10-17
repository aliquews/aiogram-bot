import requests
from bs4 import BeautifulSoup


def translit(stype) -> str:
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    return ''.join([t[i] for i in stype.lower()])


def getWeather(msg):
    city = translit(msg)
    data = requests.get(
        f'https://pogoda.mail.ru/prognoz/{city}/24hours/').text
    soup = BeautifulSoup(data, 'lxml')
    date = soup.find('div', class_='p-forecast__title').text
    temperature = soup.find(
        'span', class_='p-forecast__temperature-value').text
    description = soup.find('span', class_='p-forecast__description').text
    return f'{date}\n{temperature}C\n{description}'
