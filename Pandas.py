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




