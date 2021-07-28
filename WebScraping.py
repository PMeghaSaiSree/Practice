#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()


# In[12]:


from bs4 import BeautifulSoup
from lxml import etree
import requests
  
  
URL = "http://coreyms.com"
  
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))
print(dom.xpath('/html/body/div/div/div/main/article[1]/header/h2/a')[0].text)
#/html/body/div/div/div/main/article[1]/header/h2/a


# In[13]:


from bs4 import BeautifulSoup
from lxml import etree
import requests
  
  
URL = "http://coreyms.com"
  
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "lxml")
dom = etree.HTML(str(soup))
print(dom.xpath('/html/body/div/div/div/main/article[1]/header/h2/a')[0].text)
#/html/body/div/div/div/main/article[1]/header/h2/a


# In[10]:


from bs4 import BeautifulSoup
from lxml import etree
import requests
  
  
URL = "https://en.wikipedia.org/wiki/Nike,_Inc."
  
  
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")
dom = etree.HTML(str(soup))
print(dom.xpath('//*[@id="firstHeading"]')[0].text)


# In[ ]:




