#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py

import tweepy
import logging
from config import create_api
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class LikeListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        try:
            tweettext = str(tweet.extended_tweet['full_text'].lower().encode('ascii',errors='ignore'))
        except:
            tweettext = str(tweet.text.lower().encode('ascii',errors='ignore'))
        if tweettext.startswith("rt @") == False: #make sure this is not a retweet
            if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
                # This tweet is a reply or I'm its author so, ignore it
                return
            if not tweet.favorited:
                #like the tweet since we haven't yet
                try:
                    tweet.favorite()
                except Exception as e:
                    logger.error("Error on fav", exc_info=True)
            if not tweet.retweeted: # if the tweet has media and we haven't already retweeted then we will retweet it
                try:
                    tweet.entities["media"] #check if the tweet has media
                    tweet.retweet()
                except KeyError as k:
                    print("no media")
                    pass
                except Exception as e:
                    logger.error("Error on like and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api = create_api()
    tweets_listener = LikeListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])

if __name__ == "__main__":
    main(["san diego surfing", "#surfing", "surfing webcam san diego"])