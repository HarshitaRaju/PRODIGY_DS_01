#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


url = r'C:\Users\harsh\API_SP.POP.TOTL_DS2_en_csv_v2_443830.csv'
data = pd.read_csv(url, skiprows=4)

data.head()


# In[6]:


data_2020 = data[['Country Name', '2020']].copy()

data_2020.columns = ['Country', 'Population']

data_2020.dropna(inplace=True)

data_2020.head()


# In[7]:


plt.figure(figsize=(15, 10))

sns.barplot(x='Population', y='Country', data=data_2020.sort_values(by='Population', ascending=False).head(20))

plt.title('Top 20 Countries by Population in 2020')
plt.xlabel('Population')
plt.ylabel('Country')

plt.show()


# In[ ]:




