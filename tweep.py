import sys, os

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import parse.serialise as serialise
import parse.normalise as normalise

import store.store as store

consumer_key=""
consumer_secret=""
access_key = ""
access_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

class CustomStreamListener(StreamListener):
    
    def on_data(self, data):
        
        tweetjson = serialise.stream_handle(data).json_unserialise()
        try:
            if tweetjson["text"] and tweetjson["lang"] == "en":
                tweetuser = normalise.normalise_text(tweetjson['user']['screen_name']).normalise_twitter_json()
                tweetjson = normalise.normalise_text(tweetjson['text']).normalise_twitter_json()
                tweetjson = tweetuser + ":::" + tweetjson
                store.storetweet(tweetjson)
        except Exception, e:
            print "Serialisation issue: ", e
            fname = 'errorstore.log'
            if not os.path.isfile(fname):
                file(fname, 'a').close()
                
            try :
                tweetfile = open(fname, 'a')
                tweetfile.write(tweetjson)
                tweetfile.close()
            except Exception, e:
                print "Error log issue:", e                
            
        return True
    
    def on_status(self, status):
        print status.text

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

stream = Stream(auth,  CustomStreamListener())
stream.filter(track=['twitter'])