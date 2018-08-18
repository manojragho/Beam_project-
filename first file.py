from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import Credentials

class Listen(StreamListener):

    def on_data(self, a):
        print (a)

    def on_error(self, b):
        print(b)


if __name__=="__main__":
    a_Listen = Listen()
    authenticate = OAuthHandler(Credentials.Consumer_Key,Credentials.Consumer_Secret)
    authenticate.set_access_token(Credentials.Access_Token,Credentials.Access_Token_Secret)

    streamer = Stream(authenticate,a_Listen)
    streamer.filter(track=['trump'])
