from dotenv import load_dotenv

import backend
import twitter

load_dotenv()

from dotenv import load_dotenv
load_dotenv()

def automated():
    tweet=twitter.tweetlookup("RealCandaceO","Tweets")
    oppositeTweet=backend.googlegemini("Write the opposite of this tweet while subtly mocking it. Here is the tweet: " + tweet)
    twitter.posttweet(oppositeTweet)
