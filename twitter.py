import os
from dotenv import load_dotenv
import os
load_dotenv()

from twikit import Client

USERNAME = os.getenv('USERNAME')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Initialize client
client = Client('en-US')

client.login(
    auth_info_1=USERNAME,
    auth_info_2=EMAIL,
    password=PASSWORD
)

def posttweet(text):
    tweet=client.create_tweet(
        text=text,
    )
    return tweet

tweets = client.search_tweet('python', 'Latest')


def searchtweets(query,product):
    tweets=client.search_tweet(query, product)
    return tweets[0].text

def tweetlookup(user,type):
    user = client.get_user_by_screen_name(user)
    user=user.id
    tweets = client.get_user_tweets(user, type)
    return tweets[0].text

print(tweetlookup("RealCandaceO","Tweets"))
