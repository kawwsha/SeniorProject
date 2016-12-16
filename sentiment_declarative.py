import os
import sys
from sqlalchemy import Column, Integer, String, DateTime, Boolean, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.engine import create_engine

engine = create_engine('dburl')
Base = declarative_base()

def create_tweets_table(engine):

    Base.metadata.create_all(engine)

class TweetText(Base):
    __tablename__ = "tweet"

    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime)
    text = Column(String(250), nullable=True)
    location = Column(String(250), nullable=True)
    sentiment = Column(String(250), nullable=True)
    score = Column(String(250), nullable=True)

class Image(Base):
	__tablename__ = "image"

	id = Column(BigInteger, primary_key=True)
	media_images = Column(String(250))
	tweet_id = Column(BigInteger, ForeignKey("tweet.id"))
	contains_logo = Column(Integer, nullable=True) #0 = does not contain, 1 = contains

	tweet = relationship(TweetText)

create_tweets_table(engine)