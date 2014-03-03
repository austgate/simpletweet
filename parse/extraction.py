import nltk

from collections import defaultdict

class Extraction:
    '''
       Functions to extract parts of tweets. 
    '''
    
    def __init__(self, text):
        self.text = text
    
    def extract_nep(self):
        '''
           Function extracts the entities from the text
           @param text stream of text to be parsed
           @return set of nodes and their entities
        '''
        nep = []
        try:
            print self.text
            print type(self.text)
            for sent in nltk.sent_tokenize(str(self.text)):
                for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))): 
                    if hasattr(chunk, 'node'):
                        rnep = ' '.join(c[0] for c in chunk.leaves())
                        nep.append(self._clean_node(chunk.node)+'::'+rnep)
        except Exception:
            print "Exception raised in the parsing ", Exception.message
        
        return nep
    
    def extract_twitter (self):
        '''
            Extract authors
            Looks for the @tags in Tweets
            @param string text - incoming text string
            @return list of the authors
        '''
        tweet = []
        for author in self.text.split():
            print author
            if str(author).startswith("@"):
                tweet.append(str(author))
        
        return tweet
    
    def extract_hash (self):
        '''
            Extract hash tags. 
            Looks for hashtags and puts them into an array
            @param string text - incoming text string
            @return list of the tags
        '''
        tweet = []
        for author in self.text.split():
            if str(author).startswith('#'):
                tweet.append(str(author))
        
        return tweet

    def extract_modify (self):
        '''
            Extract hash tags. 
            Looks for hashtags and puts them into an array
            @param string text - incoming text string
            @return list of the tags
        '''
        for author in self.text.split():
            if str(author) == 'MT':
                return '1'

    
    def extract_retweet (self):
        ''' 
            Looks for RT and puts them into an array
            ? Via is also used - how can we tell if this is analogous to RT
            @param string text - incoming text string
            @return list of the tags
        '''
        for author in self.text.split():
            if str(author) == 'RT':
                return '1'
        
