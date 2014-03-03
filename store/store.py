#!/usr/bin/env python
''''
    Function to store the tweet in the db. 
    Need to normalise to pull in from other sources like LinkedIn
    
    This is an endpoint and does not forward
'''

from fstore import fdao

def storetweet(tweetdata):
    
    try:
        store = fdao('./data/tweets.txt')  
        if not store:
            raise "store doesn't exist" 

        store.load_tweets(tweetdata + "\n")
    
    except Exception, e:
        print "Storage", e
        #print "Storage Error [%d]: %s" % (e.args[0], e.args[1])



