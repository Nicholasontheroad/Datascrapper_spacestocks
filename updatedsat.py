#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


# In[ ]:


#grab urls for scraping
urls = []
urls.append(["https://finance.yahoo.com/quote/ACCMF/history?p=ACCMF", "ACCMF"])#clydespacecubsat
urls.append(["https://finance.yahoo.com/quote/GOMX.ST/history?p=GOMX", "GOMX.ST"])#Gomcubesat
urls.append(["https://finance.yahoo.com/quote/AAC.ST/history?p=AAC.ST", "AAC.ST"])#aacclydesat



# In[ ]:


#columns for the csv
columns = ['url', 'company', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
data = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# In[ ]:


for url in urls:
    r = requests.get(url[0], headers=headers)
    print('Scraping: ' + url[1])
    soup = BeautifulSoup(r.text, 'html.parser')
    dv = soup.find('div', id="Col1-1-HistoricalDataTable-Proxy")
    table = dv.find('table')
    tbody = table.find('tbody')
    tr = tbody.findAll('tr')

    for item in tr:
        td = item.findAll('td')
        # print (td[0].text)
        # print (td[1].text)
        # print (td[2].text)
        # print (td[3].text)
        # print (td[4].text)
        # print (td[5].text)
        # print (td[6].text)
        
        # Length for rows with Dividend
        if (len(td) == 7):
            data.append([url[0], url[1],td[0].text, td[1].text, td[2].text, td[3].text, td[4].text, td[5].text, td[6].text])


# In[ ]:


#print data to csv

sheet = pd.DataFrame(data, columns = columns)

print(sheet)

sheet.to_csv('./spacestocks' + time.strftime("%Y%m%d-%H%M%S") + '.csv', index=None, header=True)

