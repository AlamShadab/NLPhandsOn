#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[ ]:





# In[2]:


stop_words=set(stopwords.words("english"))
print(stop_words)


# In[3]:


example_sentence="While you are off home, shadab watches a lot of anime"
words=word_tokenize(example_sentence)
print(words)


# In[4]:


filtered_words=[]
for w in words:
    if w not in stop_words:
        filtered_words.append(w)
print(filtered_words)


# In[ ]:





# In[ ]:




