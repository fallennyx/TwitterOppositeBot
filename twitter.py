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

def posttweet(text,url):

    tweet=client.create_tweet(
        text=text,
        attachment_url=url
    )
    print("Created Tweet")
    return tweet.id


def searchtweets(query,product):
    tweets=client.search_tweet(query, product)
    return tweets[0].text

def tweetlookup(user,type):

    user = client.get_user_by_screen_name(user)
    user=user.id
    tweets = client.get_user_tweets(user, type)
    print("Successfully searched")
    return tweets[0]

def deletetweet(id):
    client.delete_tweet(id)
    print("Successfully deleted")