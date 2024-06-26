from dotenv import load_dotenv
import itertools
import time



import backend
import twitter

load_dotenv()

from dotenv import load_dotenv
load_dotenv()




def automated():
    usernames = ["paulg","tylerdurdy", "tylerdurdy", "naval", "Jason","tylerdurdy", "nntaleb","caitoz","tylerdurdy"]
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
    url='https://twitter.com/'+username+'/status/'+tweet.id
    twitter.posttweet(oppositeTweet,url)
    time.sleep(10)
    if  twitter.tweetlookup("OppositeBotNyx","Tweets").quote.id !=tweet.id:
        twitter.deletetweet(twitter.tweetlookup("OppositeBotNyx","Tweets").id)
        automated()








if __name__ == "__main__":
    automated()