#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np


# In[43]:


corpus = [
    "The cat sat on the mat",
    "A dog sat on the mat",
    "The bird flew over the tree"
]


# In[45]:


def tokenize(sent):
    return sent.lower().split()


# In[47]:


vocab = {}

for doc in corpus:
    tokens=tokenize(doc)
    for token in tokens:
        if token in vocab:
            vocab[token]+=1
        else:
            vocab[token]=1
    print(doc, tokenize(doc))


# In[49]:


vocab


# In[51]:


wor2token={ k:idx for idx,(k,v) in enumerate(vocab.items())}
token2word={ v:k for (k,v) in wor2token.items()}
token2word


# In[70]:


vocab


# In[55]:


DF=np.zeros(len(vocab))
for doc in corpus:
    tokens=set(tokenize(doc))
    for token in tokens:
        DF[wor2token[token]]+=1


# In[74]:


DF
len(vocab)


# In[80]:


IDF=np.zeros(len(vocab))
for i in range(len(vocab)):
    if DF[i]>0:
        IDF[i]=np.log(len(corpus)/DF[i])


# In[82]:


IDF


# In[84]:


# TF-IDF Computation


# In[94]:


for sent in corpus:
    tokens=tokenize(sent)
    ##### TF (w,d)  #
    TF = np.zeros(len(vocab))
    for token in tokens:
        TF[wor2token[token]]+=1
    TF/= len(tokens)
    
    TF_IDF=np.zeros(len(vocab))
    for i in range(len(vocab)):
        TF_IDF[i]=IDF[i]*TF[i]
    print(TF_IDF)
        
    


# In[ ]:


4# Relationship Between TF_IDF and Stop Words


# In[96]:


# Pour comparer entre deux phrases:
TF_IDF=np.zeros((len(corpus), len(vocab)))
for idx_sent, sent in enumerate(corpus):
    tokens=tokenize(sent)
    ##### TF (w,d)  #
    TF = np.zeros(len(vocab))
    for token in tokens:
        TF[wor2token[token]]+=1
    TF/= len(tokens)
    
    for i in range(len(vocab)):
        TF_IDF[idx_sent,i]=IDF[i]*TF[i]
    print(TF_IDF[idx_sent])


# In[118]:


#Créer une fonction de la norme de vecteur , on a besoin de ça pour calculer la cosin:
def norm(v):
    s=0
    for i in range(len(v)):
        s+=v[i]**2
    return np.sqrt(s)


# In[126]:


# créer une fonction qui calcule la similarité entre deux vecteur:

def cosine_sim(A,B):
    return np.sum(A*B)/(norm(A)*norm(B))


# In[132]:


#Appliquer la formule sémilarité (exemple 1):
corpus = [
    "The cat sat on the mat",
    "A dog sat on the mat",
    "The bird flew over the tree"
]
cosine_sim(TF_IDF[1],TF_IDF[0])


# In[130]:


#Appliquer la formule sémilarité (exemple 2):
cosine_sim(TF_IDF[1],TF_IDF[2])


# In[134]:


#Appliquer la formule sémilarité (exemple 3):
cosine_sim(TF_IDF[0],TF_IDF[2])


# In[ ]:




