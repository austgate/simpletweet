'''
   Functions to normalise parts of the txt
'''

import unicodedata

class normalise_text():
    
    def __init__(self, text):
        self.text = text
        
    def normalise_twitter_json(self):
        '''
          Remove some of the odd strings that come out of Twitter streams
        '''

        #return unicodedata.normalize('NFKD', self.text)
        return unicode(self.text).encode('utf-8')
    
    def normalise_unicode (self): 
        ''' 
           Function to get the unicode text. 
           Must accept and parse varying forms of text - latin-1 and non-latin-1 
           '''
        
        return unicodedata.normalize('NFKD', self.text)