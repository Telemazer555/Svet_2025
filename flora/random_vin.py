import requests
import bs4
import json
from bs4 import BeautifulSoup
import pprint

def get_vin():
    cookies = {
        'PHPSESSID': '2efa9cde9be9085e93fa08fa78408f6a',
        '_ga_2RP2W7M0GY': 'GS2.1.s1753783559$o8$g0$t1753783559$j60$l0$h0',
        '_ga': 'GA1.2.390338617.1753102188',
        '_gid': 'GA1.2.749198868.1753783560',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.generatorslist.com',
        'Referer': 'https://www.generatorslist.com/random/numbers/random-vin-generator',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="136", "YaBrowser";v="25.6", "Not.A/Brand";v="99", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        # 'Cookie': 'PHPSESSID=2efa9cde9be9085e93fa08fa78408f6a; _ga_2RP2W7M0GY=GS2.1.s1753783559$o8$g0$t1753783559$j60$l0$h0; _ga=GA1.2.390338617.1753102188; _gid=GA1.2.749198868.1753783560',
    }

    data = {
        'numResults': '1',
    }

    response = requests.post(
        'https://www.generatorslist.com/random/numbers/random-vin-generator/ajax',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False
    )

    content = response.json()['Content']
    soup = BeautifulSoup(content, 'html.parser')
    # Находим все элементы h5 с классом card-title
    card_titles = soup.find_all('h5', class_='card-title')

    # Создаем список значений
    values = [title.get_text() for title in card_titles]

    # Преобразуем в словарь (если нужно)2
    result_dict = {f'item_{i}': value for i, value in enumerate(values, 1)}

    # Получаем второе значение (8APN7W100MPFHV5AT)
    desired_value = values[1]  # или card_titles[1].get_text()

    # print(desired_value)  # Выведет: 8APN7W100MPFHV5AT
    return desired_value
# print(result_dict)    # Выведет словарь со всеми значениями

result = get_vin()

with open('VIN.JSON', 'w',encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)