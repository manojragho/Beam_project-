# I am using tweepy package for interaction with twitter API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

import Credentials

class Listen(StreamListener):

    def __init__(self,filename):
        self.filename = filename

    def on_data(self, a):
        with open(self.filename,'a') as write_file:
            write_file.write(a)

        print (a)

    def on_error(self, b):
        print(b)


if __name__=="__main__":
    a_Listen = Listen("tweets.txt")
    authenticate = OAuthHandler(Credentials.Consumer_Key,Credentials.Consumer_Secret)
    authenticate.set_access_token(Credentials.Access_Token,Credentials.Access_Token_Secret)

    streamer = Stream(authenticate,a_Listen)
    streamer.filter(track=['trending'])
    #a_Listen.filename = "tweets.txt"

