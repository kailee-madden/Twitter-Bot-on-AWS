#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
URL = "https://www.surfline.com/surf-report/scripps/5842041f4e65fad6a7708839"

def scrape_report(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="quiver-spot-report")
    summary = results.find("p")
    forecast = [s for s in summary]

    return forecast[1][2:-3]

def tweet_report(api, url):
    tweet = "Surf report for South SD: "+scrape_report(url)
    if len(tweet) > 280:
        char_start = 0
        char_end = 279
        while char_start < len(tweet):
            twit = tweet[char_start:char_end]
            api.update_status(status=twit)
            char_start += 280
            char_end += 280
    else:
        api.update_status(status=tweet)
    return

def main():
    api = create_api()
    tweet_report(api, URL)

if __name__ == "__main__":
    main()