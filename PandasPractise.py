#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r'C:\Users\megha\Desktop\PT7\icml_face_data.csv')


# In[95]:


data.head(5)


# In[4]:


data.tail()


# In[6]:


data.shape


# In[12]:


data.info()


# In[9]:


employees = {'name' : ('Megha', 'Devashish', 'Vijaya'), 'ID': (18884, 10005, 75640), 'location' : ('hyderabad', 'bangalore', 'delhi')}


# In[10]:


employees


# In[11]:


df = pd.DataFrame(employees)


# In[12]:


df


# In[13]:


df['name']


# In[14]:


df[['name', 'ID']]


# In[15]:


df.columns


# In[18]:


df.iloc[0]


# In[19]:


df.iloc[1,1] = 2


# In[22]:


df.loc[1,0] = 2


# In[23]:


df.loc[1]


# In[24]:


df


# In[31]:


df.iloc[[1,2], ]


# In[37]:


df.loc[[1,2], ]


# In[16]:


df.loc[[0,1], ['name', 'location']]


# In[17]:


df.iloc[[0,1], ['name', 'location']]


# In[46]:


df.loc[0:2, ['name', 'location']]


# In[48]:


df.loc[0:2, 'name': 'location']


# In[50]:


df['location'].value_counts()


# In[51]:


df.set_index('name')


# In[52]:


df.set_index('name', inplace = True)


# In[53]:


df


# In[57]:


df.loc['Megha']


# In[61]:


df.loc(0)


# In[62]:


df.iloc(0)


# In[63]:


df.sort_index()


# In[67]:


df['location'] == 'hyderabad'


# In[77]:


newdf = (df['ID'] == 18884) | (df['location'] == 'delhi')


# In[78]:


newdf


# In[83]:


filt = df['location'].isin(newdf)


# In[84]:


filt


# In[85]:


df['location']


# In[153]:


data = pd.read_csv(r'C:\Users\megha\Desktop\PT7\icml_face_data.csv', nrows = 3, names = ["c1", "c2", "c3"])


# In[154]:


data


# In[155]:


data.to_csv(r'C:\Users\megha\Desktop\icml_face_data.csv', index = False)


# In[156]:


df = pd.read_excel(r'C:\Users\megha\Desktop\July.xlsx', "Sheet1")


# In[157]:


df


# In[158]:


df = df.to_excel(r'C:\Users\megha\Desktop\July1.xlsx', sheet_name = "Sheet 1")
#df.to_excel("new.xlsx", sheet_name="stocks", index=False, startrow=2, startcol=1)


# In[159]:


df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})


# In[160]:



with pd.ExcelWriter(r'C:\Users\megha\Desktop\stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")
    


# In[161]:


weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df


# In[162]:


weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df


# In[164]:


employees = {'name' : ('Megha', 'Devashish', 'Vijaya'), 'ID': (18884, 10005, 75640), 'location' : ('hyderabad', 'bangalore', 'delhi'), 'gender' : ('f', 'm','f')}


# In[165]:


data = pd.DataFrame(employees)


# In[166]:


data


# In[169]:


data['gender_num'] = data.gender.map({'f':1, 'm':0})


# In[170]:


data


# In[175]:


data.name_length = data.name.apply(len)


# In[176]:


data


# In[1]:


import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})


def square(x):
    return x * x


df1 = df.apply(square)

print(df)
print(df1)


# In[2]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})

df1 = df.apply(np.sum, axis=0)
print(df1)

df1 = df.apply(np.sum, axis=1)
print(df1)


# In[3]:


import pandas as pd


def sum(x, y, z):
    return x + y + z


df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})

df1 = df.apply(sum, args=(1, 2))
print(df1)


# In[25]:


import pandas as pd


def sum(x, y, z, m):
    return (x + y + z) * m


df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})

df1 = df.apply(sum, args=(1, 2), m=10)
print(df1)


# In[26]:


df


# In[5]:


import pandas as pd
import math

df = pd.DataFrame({'A': [1, 4], 'B': [100, 400]})
df1 = df.applymap(math.sqrt)

print(df)
print(df1)


# In[6]:


import pandas as pd

df = pd.DataFrame({'Name': ['Pankaj', 'Meghna'], 'Role': ['ceo', 'cto']})

df1 = df.applymap(str.upper)

print(df)
print(df1)


# In[ ]:




