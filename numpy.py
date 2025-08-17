#!/usr/bin/env python
# coding: utf-8

# In[1]:


#numpy_Array
my_list = [1,2,3]
my_list


# In[2]:


import numpy as np


# In[4]:


arr = np.array(my_list)
arr


# In[6]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix


# In[7]:


np.array(my_matrix)


# In[9]:


np.arange(0,11,2)


# In[14]:


np.zeros((4,4))


# In[16]:


np.ones((3,4))


# In[19]:


np.linspace(0,10,2)


# In[20]:


np.eye(5)


# In[21]:


np.random.rand(5)


# In[25]:


np.random.randn(4,1)


# In[27]:


np.random.randint(1987,2025,10)


# In[31]:


arr = np.arange(25)
arr.reshape(5,5)


# In[30]:


ranrr = np.random.randint(0,50,10)


# In[ ]:




