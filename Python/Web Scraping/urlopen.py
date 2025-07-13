#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen


# In[5]:


def retrieve_page(url):
    return urlopen(url).read() 


# In[6]:


page = retrieve_page('https://github.com')

