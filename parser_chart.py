import requests
import json
from pprint import pprint

cookies = {
    'gdpr': '0',
    'L': 'cjd9RGNZYnB3fmZLfgNxRWNVVX5NcQwGJj0dOzoGFHkEJw0=.1662297657.15090.336073.f01954ce0040d3c0df26c0db7557a763',
    'yandex_login': 'shutova.any',
    'my': 'YwA=',
    '_ym_uid': '1667905531180763498',
    'i': 'dCoqSOGSOJF0sOpHmn+WmV7lkA0mc3ejXwdYIkbhksHzMHlNCjyy2qISHg0F9M4MokTFZ3v/kNie5XwUusm+LPGH6W8=',
    'yandexuid': '6056691441662297615',
    'yuidss': '6056691441662297615',
    'ymex': '1995542434.yrts.1680182434#1993794822.yrtsi.1678434822',
    'is_gdpr': '0',
    'is_gdpr_b': 'CIHuMRCusQEoAg==',
    'fullscreen-saved-data': '%7B%22compositeId%22%3A%22iskra-july-7%22%7D',
    'font_loaded': 'YSv1',
    'Session_id': '3:1695033712.5.0.1662297657258:V8auVQ:5.1.2:1|1103400855.-1.2.1:243969095|3:10275929.721996.MIutJR-8pAA3bVqqCddKH7xcJdQ',
    'sessar': '1.1182.CiC8AFhLR4GUuezhoe7ZfuNEPaXgzZLDfpxqTJxJyypNTg.Ddps1471ZWl655KaUnHqBxbW1AwUhOnFMjPCGJ0rYcc',
    'sessionid2': '3:1695033712.5.0.1662297657258:V8auVQ:5.1.2:1|1103400855.-1.2.1:243969095|3:10275929.721996.fakesign0000000000000000000',
    'sae': '0:26cf80bc-1bef-471b-ac63-bcd14B2DBA61:p:22.11.0.2484:l:d:RU:20220906',
    '_ym_isad': '2',
    'cycada': 'DmKZy+cRG87n+YZW86mCh161hEiYqrGefTLOjrtF0Hw=',
    'ys': 'svt.1#def_bro.1#wprid.1695215296977783-11026454504860341569-balancer-l7leveler-kubr-yp-vla-106-BAL-7206#ybzcc.ru#newsca.native_cache',
    '_yasc': '7NJw14f1/UvE1nDPQ2bTMvFlO7KV0KQuoC0EKO+Z3QKoJJdGpWccwMwmgTQ/Df3aIIGHLB40EW7r1pAUR+mMe3nn8J0=',
    'chromecast': "''",
    'lastVisitedPage': '%7B%7D',
    '_ym_d': '1695216979',
    'device_id': 'a7dd606eaa81e9cca98775c8b576570ad00f8d09c',
    'active-browser-timestamp': '1695216978784',
    'bh': 'EjciQ2hyb21pdW0iO3Y9IjEwNiIsIllhbmRleCI7dj0iMjIiLCJOb3Q7QT1CcmFuZCI7dj0iOTkiGgUieDg2IiIOIjIyLjExLjAuMjQ4NCIqAj8wOgciTGludXgiQgciNi4yLjAiSgQiNjQiUlMiQ2hyb21pdW0iO3Y9IjEwNi4wLjUyNDkuMTY4IiwiWWFuZGV4Ijt2PSIyMi4xMS4wLjI0ODQiLCJOb3Q7QT1CcmFuZCI7dj0iOTkuMC4wLjAiIg==',
    '_ym_visorc': 'b',
    'yp': '1695282527.uc.us#1695282527.duc.ru#1711718434.cld.2574584#1977657657.udn.cDpzaHV0b3ZhLmFueQ%3D%3D#2010575298.pcs.0#1698314943.pgp.5_27779649#1697670153.hdrc.1#1713728242.stltp.serp_bk-map_1_1682192242#1705954297.szm.1_25:1536x864:1430x762#1695389900.gpauto.43_401355:39_980457:140:1:1695217090',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': "gdpr=0; L=cjd9RGNZYnB3fmZLfgNxRWNVVX5NcQwGJj0dOzoGFHkEJw0=.1662297657.15090.336073.f01954ce0040d3c0df26c0db7557a763; yandex_login=shutova.any; my=YwA=; _ym_uid=1667905531180763498; i=dCoqSOGSOJF0sOpHmn+WmV7lkA0mc3ejXwdYIkbhksHzMHlNCjyy2qISHg0F9M4MokTFZ3v/kNie5XwUusm+LPGH6W8=; yandexuid=6056691441662297615; yuidss=6056691441662297615; ymex=1995542434.yrts.1680182434#1993794822.yrtsi.1678434822; is_gdpr=0; is_gdpr_b=CIHuMRCusQEoAg==; fullscreen-saved-data=%7B%22compositeId%22%3A%22iskra-july-7%22%7D; font_loaded=YSv1; Session_id=3:1695033712.5.0.1662297657258:V8auVQ:5.1.2:1|1103400855.-1.2.1:243969095|3:10275929.721996.MIutJR-8pAA3bVqqCddKH7xcJdQ; sessar=1.1182.CiC8AFhLR4GUuezhoe7ZfuNEPaXgzZLDfpxqTJxJyypNTg.Ddps1471ZWl655KaUnHqBxbW1AwUhOnFMjPCGJ0rYcc; sessionid2=3:1695033712.5.0.1662297657258:V8auVQ:5.1.2:1|1103400855.-1.2.1:243969095|3:10275929.721996.fakesign0000000000000000000; sae=0:26cf80bc-1bef-471b-ac63-bcd14B2DBA61:p:22.11.0.2484:l:d:RU:20220906; _ym_isad=2; cycada=DmKZy+cRG87n+YZW86mCh161hEiYqrGefTLOjrtF0Hw=; ys=svt.1#def_bro.1#wprid.1695215296977783-11026454504860341569-balancer-l7leveler-kubr-yp-vla-106-BAL-7206#ybzcc.ru#newsca.native_cache; _yasc=7NJw14f1/UvE1nDPQ2bTMvFlO7KV0KQuoC0EKO+Z3QKoJJdGpWccwMwmgTQ/Df3aIIGHLB40EW7r1pAUR+mMe3nn8J0=; chromecast=''; lastVisitedPage=%7B%7D; _ym_d=1695216979; device_id=a7dd606eaa81e9cca98775c8b576570ad00f8d09c; active-browser-timestamp=1695216978784; bh=EjciQ2hyb21pdW0iO3Y9IjEwNiIsIllhbmRleCI7dj0iMjIiLCJOb3Q7QT1CcmFuZCI7dj0iOTkiGgUieDg2IiIOIjIyLjExLjAuMjQ4NCIqAj8wOgciTGludXgiQgciNi4yLjAiSgQiNjQiUlMiQ2hyb21pdW0iO3Y9IjEwNi4wLjUyNDkuMTY4IiwiWWFuZGV4Ijt2PSIyMi4xMS4wLjI0ODQiLCJOb3Q7QT1CcmFuZCI7dj0iOTkuMC4wLjAiIg==; _ym_visorc=b; yp=1695282527.uc.us#1695282527.duc.ru#1711718434.cld.2574584#1977657657.udn.cDpzaHV0b3ZhLmFueQ%3D%3D#2010575298.pcs.0#1698314943.pgp.5_27779649#1697670153.hdrc.1#1713728242.stltp.serp_bk-map_1_1682192242#1705954297.szm.1_25:1536x864:1430x762#1695389900.gpauto.43_401355:39_980457:140:1:1695217090",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2484 Yowser/2.5 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.4346034032624708',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers).json()

with open('chart.json', 'w') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)

with open('chart.json', 'r') as f:
    chart = json.load(f)

parsed_chart = dict()
for i, track_info in enumerate(chart['chartPositions']):
    track = track_info['track']
    parsed_chart[i + 1] = {tuple([artist['name'] for artist in track['artists']]): track['title']}

pprint(parsed_chart)
