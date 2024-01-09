from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import time
import pandas as pd
with open('url_list.txt', 'r') as file:
    url_list = list(file.readlines())

#getting rid of \n
for i in range(len(url_list)):
    url_list[i] = url_list[i][:-1]

#checking if there are any duplicates and deleting them
url_df = pd.DataFrame(url_list, columns=['url'])
print(df.value_counts(), len(df))

url_df.drop_duplicates(inplace=True)

# for link in url_df['url']:
#     print(link)

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

df = pd.DataFrame(columns=['cena',
                           'powierzchnia',
                           'liczba_pokoi',
                           'stan_wykonczenia',
                           'balkon_ogrod_taras',
                           'czynsz',
                           'miejsce_parkingowe',
                           'ogrzewanie',
                           'lokalizacja'])

for link in url_df['url']:
    try:
        request = Request(link, headers=headers)

        html = urlopen(request)
        bs = BeautifulSoup(html.read(), 'html.parser')

        record_dict = {}

        # scrapowanie ceny mieszkania
        interest = bs.find('strong', attrs={'class': "css-t3wmkv e1l1avn10"})
        try:
            record_dict['cena'] = int(interest.text[:-3].replace(' ', ''))
        except ValueError:
            record_dict['cena'] = None

        # parametry mieszkania
        interest = bs.find('div', attrs={'class': "css-2vlfd7 e10umaf20"})
        info = interest.find_all('div', attrs={'class':"css-1qzszy5 enb64yk2"})

        try:
            record_dict['powierzchnia'] = float(((info[1].text)[:-3]).replace(',', '.'))
        except ValueError:
            record_dict['powierzchnia'] = None

        try:
            record_dict['liczba_pokoi'] = int(info[5].text)
        except ValueError:
            record_dict['liczba_pokoi'] = None

        record_dict['stan_wykonczenia'] = info[7].text
        if record_dict['stan_wykonczenia'] == 'Zapytaj':
            record_dict['stan_wykonczenia'] = None

        record_dict['balkon_ogrod_taras'] = info[11].text
        if record_dict['balkon_ogrod_taras'] == 'Zapytaj':
            record_dict['balkon_ogrod_taras'] = None

        try:
            record_dict['czynsz'] = int((info[13].text)[:-3].replace(' ', ''))
        except:
            record_dict['czynsz'] = None

        record_dict['miejsce_parkingowe'] = info[15].text
        if record_dict['miejsce_parkingowe'] == 'Zapytaj':
            record_dict['miejsce_parkingowe'] = None

        record_dict['ogrzewanie'] = info[19].text
        if record_dict['ogrzewanie'] == 'Zapytaj':
            record_dict['ogrzewanie'] = None

        record_dict['lokalizacja'] = bs.find('a', attrs={'class': "e1w8sadu0 css-1helwne exgq9l20"}).text

        df.loc[len(df)] = record_dict
        print(f"Record {len(df)} added.")
        time.sleep(0.4)
    except Exception as e:
        print('Error: ', e)

df.to_csv('data_to_analyze.csv')
