#!/usr/bin/env python
# tweepy-bots/bots/followfollowers.py

import tweepy
from config import create_api
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    api = create_api()
    since_id = 1
    while True:
        follow_followers(api)
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(360)

def follow_followers(api):
    logger.info("Retrieving followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following: follower.follow()

def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if not tweet.user.following:
            tweet.user.follow()
    return new_since_id

if __name__ == "__main__":
    main()