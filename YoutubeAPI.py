#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib
import urllib.request
import urllib3
import json
import string
import random


# In[2]:


import csv


# In[3]:


def Create_Video_Link(videoID):
    
    string1 = ''

    url = ["https://www.youtube.com/watch?v="]
    url.insert(1, videoID)
    urlstring = string1.join(url)
    return urlstring


# In[5]:


import json
import urllib.request
import string

def GVD(count, API_KEY, csvfile, search_query):
    import random


    count = count
    API_KEY = API_KEY
    if search_query == 0:
        random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
    else:
        random = search_query

    urlData = " https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,random)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    with open(csvfile, mode='w', encoding='utf-8') as csvfile:
            fieldnames = ['video_link', 'description', 'videoID']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in results['items']:
                videoId = (data['id']['videoId'])
                link = Create_Video_Link(videoId)
                print (link)
                description = (data['snippet']['description'])
                print (description)
                writer.writerow({"video_link": link, "description": description, "videoID": videoId})


# In[6]:


GVD(400,'AIzaSyAu6IO4hqnZ3e9zHnbbhpwlowb-FK358Y8', 'video_data3.csv', 'gsu32923')


# In[ ]:




