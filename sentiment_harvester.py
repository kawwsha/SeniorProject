# -*- coding: utf-8 -*-

import tweepy
import json

from watson_developer_cloud import AlchemyLanguageV1
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sentiment_declarative import TweetText, Image, Base

alchemy_language = AlchemyLanguageV1(api_key='apikey')

class TweepyAuth(object):

    """
        Our TweepyAuth class that manages the creation of
        a tweepy.OAuthHandler object needed for the initialization
        of a tweepy.API instance.
    """

    def __init__(self,
                 consumer_key='consumerkey',
                 consumer_secret='consumersecret',
                 access_token='accesstoken',
                 access_token_secret='accesssecret'):

        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

        
class TweetHarvester(object):

    """
        This class harvests Tweets. It relies on a default
        TweepyAuth.auth object at init.
    """

    def __init__(self, auth=TweepyAuth().auth):
        self.__api = tweepy.API(auth)

    def posts(self, tag, num_items=10):

        """
            This method is a generator that encapsulates the Tweepy search method.
            It yields our custom Tweet objects.

            This will retrieve 10 items by default. Increase or decrease as needed,
            and know of Twitter API rate limiting for super large queries.
        """

        for tweet in tweepy.Cursor(self.__api.search, q=tag).items(num_items):
            if "media" in tweet.entities:
                yield Tweet(tweet.created_at,
                            tweet.id_str,
                            tweet.text,
                            tweet.user.location,
                            [m["media_url_https"] for m in tweet.entities["media"]])


class Tweet(object):

    def __init__(self, created_at, id_str, text, location, media_images):
        self.created_at = created_at
        self.id_str = id_str
        self.text = text.encode('ascii', 'ignore').decode('ascii')
        self.location = location.encode('ascii', 'ignore').decode('ascii')
        self.media_images = media_images[0]
        self.twitter_url = 'twitter.com/anyuser/status/' + id_str



def main():

    engine = create_engine('dburl')
    Base.metadata.bind = engine
    DBASession = sessionmaker(bind=engine)
    session = DBASession()

    t = TweetHarvester()
    for p in t.posts("starbucks", num_items=2000):

        json_dump = (json.dumps(alchemy_language.sentiment(url=p.twitter_url), indent=2))
        json_string = json.loads(json_dump)
        #print (json_string)
        sentiment_type = json_string['docSentiment']['type']
        if sentiment_type in ['negative', 'postive']:
            sentiment_score = json_string['docSentiment']['score']
        else:
            sentiment_score = '0'
        #print (sentiment_score)

        new_tweet = TweetText(id = p.id_str, created_at=p.created_at, text=p.text, location=p.location, score= sentiment_score, sentiment= sentiment_type)
        session.add(new_tweet)
        session.commit()

        new_image = Image(tweet_id= p.id_str, media_images=p.media_images)
        session.add(new_image)
        session.commit()
    
if __name__ == '__main__':
    main()
