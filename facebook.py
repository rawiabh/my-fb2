
# coding: utf-8

# In[ ]:


from flask import Flask
import json
import urllib.request as ur
import requests
app = Flask(__name__)

token= "EAACRyxtuJXcBAFZCuhpkL8FfrgEDWtsa5LVT8DVGGpCZA68AdxqfJv6YI5RotUtqsZBHrEAKGcpcQxZCZBroonZCXeC2MYgBzBlvZCg4W05fF8sb5Tc8vt0KPDsaq7gQXamZBrs45XRPFEJ5yvp36SfnZBZC2lbbx9EjxkJ6Pqeg1rtTK4n6W1SJZAt9QvPbRLSda5IvZBwCf2OwiQZDZD"
me="https://graph.facebook.com/v2.10/me?access_token="+token
friends="https://graph.facebook.com/v2.10/me/friends?access_token="+token
search="https://graph.facebook.com/v2.10/search?q=zara&type=page&access_token="+token

@app.route('/')
def hello_world():
    res=requests.get(search)
    return res.text

if __name__ == '__main__':
  app.run()

