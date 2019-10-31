#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime

import sys
sys.path.append('../../../..')

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
weather_api_key = os.environ.get("weather_api_key")


# In[ ]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[ ]:


# Weather API Key
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "Washington, D.C."
units = "imperial"
query_url = url + "appid=" + weather_key + "&q=" + city + "&units=" + units


# In[ ]:


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    query_url = url + "appid=" + weather_key + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    r = req.get(query_url).json()
    temp = r['main']['temp']

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(f"Current temperature in {city}: {temp}F")

    # Print success message
    print('Weather tweet posted')


# In[ ]:


# Set timer to run every 1 hour
while(True):
    WeatherTweet()
    time.sleep(60*60)


# In[ ]:




