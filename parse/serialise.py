'''
   Functions to deal with XML and JSON streams
'''
import json

class stream_handle():
    
    def __init__(self, stream):
        '''
           Stream may be a an XML/JSON stream or a Python object
           '''
        self.stream = stream
        
    def json_unserialise(self):
        '''
           Decode stream
           @param json stream
           @return Python array object
        '''
        return json.loads(self.stream)
    
    def json_serialise(self):
        '''
           Function to return the JSON string of a Python object
        '''
        return json.dumps(self.stream)