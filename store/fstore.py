import os

class fdao:
    
    def __init__(self, fname):
        self.filename = fname
        
        if not os.path.isfile(fname):
            file(fname, 'w+').close()
    
    def load_tweets(self, data):
        
        try :
            tweetfile = open('./data/tweets.txt', 'a')
            tweetfile.write(data)
            tweetfile.close()
        except Exception, e:
            print "File Store issue:", e