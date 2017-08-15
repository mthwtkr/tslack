from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from twitter import Twitter, OAuth

class Twitter():
    def __init__():
        oauth = OAuth(
            settings.ACCESS_TOKEN, 
            settings.ACCESS_SECRET, 
            settings.CONSUMER_KEY, 
            settings.CONSUMER_SECRET
        )
        self.twitter = Twitter(auth=oauth)

    def search(hashtag):
        return self.twitter.search.tweets(q=hashtag)
