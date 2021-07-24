#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
r = requests.get('https://xkcd.com/353/')
#print(r.status_code)
#print(r.text)

image = requests.get('https://imgs.xkcd.com/comics/python.png')
#print(image.content)
print(image.ok)

with open ('comic.png', 'wb') as f:
    f.write(image.content)
    
payload = {'page' : 5, 'count' : 10, 'number' : 7}
r = requests.get('https://httpbin.org/get', params = payload)
#print(r.text)
print(r.url)

payload = {'name' : 'megha', 'id' : 18884}
r = requests.post('https://httpbin.org/post', data = payload)
#print(r.text)

payload = {'name' : 'megha', 'id' : 18884}
r = requests.put('https://httpbin.org/put', data = payload)
#print(r.text)
#print(r.json())

r = requests.get('https://httpbin.org/basic-auth/megha/18884', auth = ('megha', 18884))
#print(r.text)

r = requests.get('https://httpbin.org/delay/1', timeout = 2)
print(r)


# In[2]:


import requests
url = requests.get('https://towardsdatascience.com/best-5-free-stock-market-apis-in-2019-ad91dddec984')
print(url.status_code)
#print(url.text)
#print(url.content)
urlImage = requests.get('https://miro.medium.com/max/1400/0*FuN-4mH9hm0QdJWm')
print(urlImage)


# In[14]:


import requests
r = requests.get('https://money.cnn.com/data/markets')
print(r.status_code)
#print(r.headers)
print(r.text)


# In[4]:


#QJWBKRCLMASEBYEW

import requests
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=QJWBKRCLMASEBYEW/get')
print(r.status_code)
#print(r.headers)
print(r.text)
#print(r.content)


# In[16]:


import requests
r = requests.get('https://api.github.com/events')
events = r.json()
#print(events)
i = 1
for i in events:
    print(i['id'])


# In[5]:


pip install GOOGLEFINANCE


# In[6]:


import GOOGLEFINANCE as gf
gf("GOOG", "price")
gf(ticker, [attribute], [start_date], [end_date|num_days], [interval])


# In[7]:


pip install yfinance


# In[8]:


import yfinance as yf

aapl = yf.Ticker("AAPL")
print(aapl)
"""
returns
<yfinance.Ticker object at 0x1a1715e898>
"""

# get stock info
aapl.info

"""
returns:
{
 'quoteType': 'EQUITY',
 'quoteSourceName': 'Nasdaq Real Time Price',
 'currency': 'USD',
 'shortName': 'Microsoft Corporation',
 'exchangeTimezoneName': 'America/New_York',
  ...
 'symbol': 'MSFT'
}
"""

# get historical market data, here max is 5 years.
aapl.history(period="max")


# In[9]:


pip install alpha_vantage


# In[ ]:


import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'QJWBKRCLMASEBYEW'
ts = TimeSeries(key=api_key, output_format='json')
#ts = TimeSeries(key=api_key, output_format='pandas')
data, metadata = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
#print(data)

while True:
    data, metadata = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
    new = pd.DataFrame.from_dict(data)   #converting dictionary to dataframe
    print(new)
    new.to_excel(r"C:\Users\megha\Desktop\July.xlsx")
    #data.to_excel(r"C:\Users\megha\Desktop\July.xlsx")
    time.sleep(60)
    
    

    


# In[11]:


type(data)


# In[12]:


import requests
payload = {'function' :'TIME_SERIES_INTRADAY', 'symbol' : 'IBM', 'interval' : '1min', 'apikey' : 'QJWBKRCLMASEBYEW'}
r = requests.get('https://www.alphavantage.co/query?function', params = payload)
#r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=QJWBKRCLMAS')
print(r.status_code)
#print(r.content)
print(r.json())


# In[ ]:




