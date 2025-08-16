#!/usr/bin/env python
# coding: utf-8

# In[28]:


get_ipython().system('python -m spacy download en_core_web_sm')


# In[13]:


import spacy
nlp = spacy.load("fr_core_news_sm")
doc = nlp("Les étudiants travaillent beaucoup, mais ils aiment apprendre de nouvelles choses !")
print([t.lemma_ for t in doc if not t.is_stop and not t.is_punct])


# In[15]:


import sys
get_ipython().system('{sys.executable} -m spacy download fr_core_news_md')


# In[17]:


import spacy

# Charger le modèle français moyen
nlp = spacy.load("fr_core_news_md")

# Exemple
doc = nlp("Les étudiants travaillent beaucoup, mais ils aiment apprendre de nouvelles choses !")
print([t.lemma_ for t in doc if not t.is_stop and not t.is_punct])


# In[19]:


# --- Installation du modèle français (md) ---
import sys
get_ipython().system('{sys.executable} -m spacy download fr_core_news_md')

# --- Chargement du modèle ---
import spacy
nlp = spacy.load("fr_core_news_md")

# --- Fonction de prétraitement ---
def preprocess_text(text: str) -> str:
    doc = nlp(text.lower())
    tokens = [t.lemma_ for t in doc if not t.is_stop and not t.is_punct]
    return " ".join(tokens)

# --- Test ---
texte = "Les étudiants travaillent beaucoup, mais ils aiment apprendre de nouvelles choses !"
print("Entrée :", texte)
print("Sortie :", preprocess_text(texte))


# In[21]:


nlp = spacy.load('en_core_web_sm')
doc = nlp(text1)


# In[33]:


text1 = """I love sci-fi and am willing to put up with a lot. Sci-fi movies/TV are usually underfunded, under-appreciated and misunderstood. I tried to like this, I really did, but it is to good TV sci-fi as Babylon 5 is to Star Trek (the original). Silly prosthetics, cheap cardboard sets, stilted dialogues, CG that doesn't match the background, and painfully one-dimensional characters cannot be overcome with a 'sci-fi' setting. (I'm sure there are those of you out there who think Babylon 5 is good sci-fi TV. It's not. It's clichéd and uninspiring.) While US viewers might like emotion and character development, sci-fi is a genre that does not take itself seriously (cf. Star Trek). It may treat important issues, yet not as a serious philosophy. It's really difficult to care about the characters here as they are not simply foolish, just missing a spark of life. Their actions and reactions are wooden and predictable, often painful to watch. The makers of Earth KNOW it's rubbish as they have to always say "Gene Roddenberry's Earth..." otherwise people would not continue watching. Roddenberry's ashes must be turning in their orbit as this dull, cheap, poorly edited (watching it without advert breaks really brings this home) trudging Trabant of a show lumbers into space. Spoiler. So, kill off a main character. And then bring him back as another actor. Jeeez! Dallas all over again."""


# In[41]:


nlp = spacy.load('en_core_web_sm')
doc = nlp(text1.lower())


# In[51]:


vocab_tmp = []
for token in doc:
    if not (token.is_stop or token.is_punct):
        vocab_tmp.append(token.text)


# In[53]:


len(set(vocab_tmp))


# In[59]:


vocab_inv = {v:k for k,v in vocab.items()}


# In[61]:


vocab_inv


# In[57]:


vocab = {k:v for v,k in enumerate(set(vocab_tmp))}
vocab


# In[ ]:


#BOG OF WORDS


# In[63]:


text1.lower().split()


# In[85]:


text3="""I usually enjoy sci-fi and can forgive a lot, but this was just awful. The sets looked cheap, the dialogue was stiff, and the characters had no life at all. It tried to be profound, but ended up clichéd and boring. Honestly, it felt more like a parody than real sci-fi."""


# In[87]:


len(text3.lower().split())


# In[89]:


import numpy as np
vec=np.zeros(len(vocab))
for key in vocab:
    if key in text3.lower().split():
        vec[vocab[key]]+=1


# In[73]:


vec


# In[91]:


np.where(vec==1)


# In[107]:


[vocab_inv[idx] for idx in np.where(vec==1)[0]]


# In[109]:


import os
print(os.getcwd())


# In[111]:


import shutil

# chemin d'origine (fichier à déplacer)
src = "/Users/khadidjabaaziz/install spacy.ipynb"

# destination (où tu veux coller le fichier)
dst = "/Users/khadidjabaaziz/Desktop/Machine_learning/install spacy.ipynb"

# déplacer le fichier (coupé-collé)
shutil.move(src, dst)

print("✅ Fichier déplacé avec succès !")


# In[ ]:




