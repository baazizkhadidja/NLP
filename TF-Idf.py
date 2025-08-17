#!/usr/bin/env python
# coding: utf-8

# In[5]:


corpus = ["mam is still my mam",
         "the is no there there",
         "mam is a mam is a mam is a mam"]


# In[6]:


#First we use pandas to get the term-frequency matrix:
import pandas as pd
from collections import Counter


# In[7]:


tf = pd.DataFrame(
    [pd.Series(Counter(doc.split())) for doc in corpus],
).fillna(0)
tf


# In[55]:


#Implementing the Vector Space Model

import numpy as np

def length(v):
    return np.sqrt((v ** 2).sum())

def cos_dist(v, w):
    return (v * w).sum() / (length(v) * length(w))

cos_dist(tf.loc[0], tf.loc[1]), cos_dist(tf.loc[0], tf.loc[2])


# In[65]:


#forte similarité entre doc1 et doc3


# In[ ]:


#tf : term frequency : nombre de terme dans document / le nombre totale des mots dans ce meme document 
#idf : iverse document frequency : facteur de rareté : + il est important : + le mot est rare 
#idf =le log de (nombre totale des document dans le corpus/le nombre des documents qui contiennent le mot clé)
# si le mot est très frèquent -> la division diminue et rapproche à 1 -> le log rapproche à zero 
# on ajoute ce facteur de rareté à notre règle pour plus de précision (que le terme soit vraiment rare)


# In[ ]:


#   tf-idf = tf(d,t)*idf(t, D)  -> on compte le nombre de terme dans un document plus sa rareté 

