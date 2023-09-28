import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep
import json

cookies = {
    'PHPSESSID': '8nen93k21nbmuqafpvj6ksm5s7',
    '51a55dae53577255b792d39bfe1d40ac': '1',
    '_ga': 'GA1.1.1465359448.1695899733',
    '_ym_uid': '1695899734667530793',
    '_ym_d': '1695899734',
    '_ym_isad': '2',
    '_ga_BB3QC8QLF4': 'GS1.1.1695899733.1.1.1695899919.0.0.0',
}

headers = {
    'authority': 'zaka-zaka.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=8nen93k21nbmuqafpvj6ksm5s7; 51a55dae53577255b792d39bfe1d40ac=1; _ga=GA1.1.1465359448.1695899733; _ym_uid=1695899734667530793; _ym_d=1695899734; _ym_isad=2; _ga_BB3QC8QLF4=GS1.1.1695899733.1.1.1695899919.0.0.0',
    'referer': 'https://jazz.sber.ru/',
    'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2484 Yowser/2.5 Safari/537.36',
}
all_games = {}

for i in range(1, 16):
    print(f'page {i}')
    response = requests.get(f'https://zaka-zaka.com/game/new/page{i}', cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    blocks = soup.find_all('a', class_='game-block')
    for block in blocks:
        if 'game-block-more' in block.get('class'):
            continue
        title = block.find('div', class_='game-block-name').text
        price = float(block.find('div', class_='game-block-price').text[:-1])
        all_games[title] = price
    sleep(1)

with open('new_catalog.json', 'w') as file:
    json.dump(all_games, file, indent=4)
