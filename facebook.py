
# coding: utf-8

# In[23]:


token= "EAACRyxtuJXcBAI1FeyL8nHuhhMogYneKEdmZAcCwfC31bhzlhfzvvX0EYxlKlrSLZBQ9t9dfgBWYZCh6KWmrJojtr9SItSZArGCaUnmMj5SRi3K7oMh7eyjKdEAqGeOOEXrsQk4GDAoXPFh4D6d6ALam3v6ZAcbqGaJ99GQ3ZAWPIdV53RZAocjYI7kOY7Ief8rl0bq8ZCweBAZDZD"
me="https://graph.facebook.com/v2.10/me?access_token="+token
friends="https://graph.facebook.com/v2.10/me/friends?access_token="+token
search="https://graph.facebook.com/v2.10/search?q=zara&type=page&access_token="+token


# In[24]:


import json
import urllib.request as ur
import requests
res=requests.get(search)
res.text


