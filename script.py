from dotenv import load_dotenv
import itertools
import time



import backend
import twitter

load_dotenv()

from dotenv import load_dotenv
load_dotenv()




def automated():
    usernames = ["RealCandaceO", "paulg","tylerdurdy", "naval", "Jason","tylerdurdy", "nntaleb","AnnCoulter","caitoz","Cernovich","LauraLoomer","tylerdurdy"]
    usernames_cycle = itertools.cycle(usernames)
    username=next(usernames_cycle)
    tweet=twitter.tweetlookup(username,"Tweets")
    while len(tweet.text)>250:
        username=next(usernames_cycle)
        tweet=twitter.tweetlookup(username,"Tweets")

    tweetText=tweet.text
    oppositeTweet=backend.googlegemini("In 230 characters or less,Write a tweet that is shorter but opposite version of this tweet while subtly mocking it. Here is the tweet: " + tweetText)
    while len(oppositeTweet)>250:
        oppositeTweet=backend.googlegemini("In 230 characters or less,Write a tweet that is shorter but opposite version of this tweet while subtly mocking it. Here is the tweet: " + tweetText)
    url="x.com/"+username+"/status/"+tweet.id
    twitter.posttweet(oppositeTweet,url)
    print("Tweet posted")



if __name__ == "__main__":
    automated()