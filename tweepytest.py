#!/usr/bin/python3

import tweepy
import json

class StreamObject(tweepy.StreamListener):
    def _init_(self, api):
        self.api = api
        self.me = api.me()
    
    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def error_message(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("GuYZVy8pBW5mEqGgdTTAwxwYZ", 
    "PFXbddDdZ1ZSnrybVRIYiP4eZJfB92DO8F4NcK964Up9oKzoGb")
auth.set_access_token("1264288620807991296-8PD5SWe0iWeNoGXQkJNjhVmCfxpFQK", 
    "PXk7oDkuBbNMzwRMwo3Ujpm8hkwOAH2M0Pd9avoE7qQ2Q")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#api.update_status("Test tweet from Tweepy Python")
#api.update_profile(description = "San Diego surf conditions and relevant news!")

for follower in tweepy.Cursor(api.followers).items():
    follower.follow() #follow whoever is following me

#api.create_favorite(tweet.id)

for tweet in api.search(q="'San Diego' #surfing -filter:retweets", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

#tweets_listener = StreamObject(api)
#stream = tweepy.Stream(api.auth, tweets_listener)
#stream.filter(track=["San Diego", "surfing", "#surfing"], languages=["en"])

#tweets = api.mentions_timeline()
#for tweet in tweets:
 #   tweet.favorite()
  #  tweet.user.follow() #follow and like any tweets that mention me