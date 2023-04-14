import requests
import http.cookiejar as cookiejar
import json
from bs4 import BeautifulSoup
url = "https://www.tiktok.com/cs-CZ/"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8','Origin': 'https://www.tiktok.com',
    'Referer': 'https://www.tiktok.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
payload = {
    'username': 'sysadminn',
    'password': 'password'
}
session = requests.session()
session.headers = headers
g

r = session.get(url, data=payload)
print(r)
soup = BeautifulSoup(r.content, 'html.parser')
content = soup.find('div', {'class': 'tiktok-14aeum4-DivContentContainer exfus56'})
if content:
    username = content.find('a').text
    print(username)
else:
    print('cant reach this url')

