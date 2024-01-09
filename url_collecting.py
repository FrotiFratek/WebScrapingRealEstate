from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import time

url_pages = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/malopolskie/krakow/krakow/krakow?limit=24&ownerTypeSingleSelect=ALL&by=DEFAULT&direction=DESC&viewType=listing&page='

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

for i in range(1, 305):
    url_current_page = url_pages + str(i)
    request = Request(url_current_page, headers=headers)

    html = urlopen(request)
    bs = BeautifulSoup(html.read(), 'html.parser')

    interest = bs.find_all('a', attrs={'class':"css-lsw81o e1dfeild2"})
    for item in interest[3:]:
        with open('url_list.txt', 'a') as file:
            file.write('https://www.otodom.pl' + str(item['href']) + '\n')
    print(f'Page {i} done.')
    time.sleep(0.4)
