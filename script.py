from dotenv import load_dotenv
import itertools
import time



import backend
import twitter

load_dotenv()

from dotenv import load_dotenv
load_dotenv()




def automated():
    usernames = ["RealCandaceO", "paulg", "naval", "Jason", "nntaleb","AnnCoulter","caitoz","Cernovich","LauraLoomer"]
    usernames_cycle = itertools.cycle(usernames)
    username=next(usernames_cycle)
    tweet=twitter.tweetlookup(username,"Tweets")
    oppositeTweet=backend.googlegemini("Write the exact opposite of this tweet while subtly mocking it. Here is the tweet: " + tweet)
    twitter.posttweet(oppositeTweet)



if __name__ == "__main__":
    automated()