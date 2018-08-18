import tweepy
import Credentials
import json

auth = tweepy.OAuthHandler(Credentials.Consumer_Key,Credentials.Consumer_Secret)
auth.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
api = tweepy.API(auth)

india_trending = api.trends_place(23424848)

print(india_trending)