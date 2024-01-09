from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

url_current_page = 'https://www.otodom.pl/pl/oferta/4-pok-kuchnia-2-lazienki-balkon-garaz-wieliczka-ID4nVOv'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

request = Request(url_current_page, headers=headers)

html = urlopen(request)
bs = BeautifulSoup(html.read(), 'html.parser')

#scrapowanie ceny mieszkania
interest = bs.find('strong', attrs={'class':"css-t3wmkv e1l1avn10"})

print(int(interest.text[:-3].replace(' ', '')))

#parametry mieszkania
interest = bs.find('div', attrs={'class':"css-2vlfd7 e10umaf20"})

info = interest.find_all('div', attrs={'class':"css-1qzszy5 enb64yk2"})
for item in info:
      print(item.text)

interest = bs.find('a', attrs={'class':"e1w8sadu0 css-1helwne exgq9l20"})

print(interest.text)



