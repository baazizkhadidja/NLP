#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array(my_list)
d = {'a':10, 'b':20, 'c':30}


# In[5]:


pd.Series(data=my_list, index=labels)


# In[7]:


pd.Series(arr, labels)


# In[8]:


pd.Series(d)


# In[10]:


ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany', 'USSR', 'Japan'])
ser1


# In[13]:


ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany', 'Italy', 'Japan'])


# In[14]:


ser3 = pd.Series(data = labels)


# In[15]:


ser1+ser2


# In[ ]:


#Pandas DataFrame


# In[18]:


from numpy.random import randn


# In[20]:


np.random.seed(101)


# In[22]:


df = pd.DataFrame(randn(5,4), index=['A','B','C','D','E'], columns = 'W X Y Z'.split())
df


# In[24]:


df['W']


# In[25]:


type(df['W'])


# In[26]:


df[['W','Z']]


# In[27]:


df['New'] = df['W']+df['Y']


# In[28]:


df['New']


# In[29]:


df


# In[35]:


df.drop('New', axis = 1, inplace=True)


# In[36]:


df


# In[39]:


df.drop('B', inplace=True)


# In[40]:


df


# In[41]:


df.loc['A']


# In[43]:


df.iloc[2]


# In[44]:


df


# In[48]:


df.loc[['A','E'],['W','Z']]


# In[ ]:




