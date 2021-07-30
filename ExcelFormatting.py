#!/usr/bin/env python
# coding: utf-8

# In[103]:


import pandas as pd
data = pd.read_excel(r'C:\Users\megha\Desktop\Try.xlsx')
data.head()


# In[104]:


df = data.groupby(['Version','Severity'])


# In[105]:


df


# In[106]:


#res[['Count']] = df['Severity'].count()
res = df['Severity'].count()
res


# In[107]:


type(res)


# In[108]:


res1 = res.to_frame()
res1


# In[109]:


res1 = res1.to_excel(r'C:\Users\megha\Desktop\Result.xlsx', sheet_name = 'Sheet1')


# In[84]:


#res1['Total'] = res1['Severity'].value_counts()
res1['Total'] = res1['Severity'].count()


# In[85]:


res1


# In[86]:


#for i in range(len(res1)):
#   res2 = res1.groupby('Version')['Severity'].sum()[1]
#res2

#res1.loc[res1['Version'] == 1, 'Severity'].sum()

#res1.query("Component" == "a")['Severity'].sum()

#import numpy as np
#print(np.where(res1['Component']=='a', res1['Severity'],0).sum())

for index, row in res1.iterrows():
     res2 = res1.groupby('Version')['Severity'].sum()[1]
res2


# In[87]:


#res1['Total'] = res1.shape[0]


# In[88]:


#res1


# In[89]:


result = res1.loc[['a','b', 'c']].sum()


# In[90]:


result


# In[91]:


res2 = res1.to_excel(r'C:\Users\megha\Desktop\Result.xlsx', sheet_name = 'Sheet1')


# In[ ]:




