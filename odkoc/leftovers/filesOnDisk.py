'''
Created on 4 apr. 2017

@author: GerbenRienk
'''

class propertiesFile():
    '''
    class to read constants / properties from a file, such as username, password, url, studyidentifier 
    all into a dictionary
    '''


    def __init__(self, propFileName):
        '''
        Constructor
        '''
        self.my_dictionary = {}
        # read the file from disk
        with open(propFileName) as f:
            for line in f:
                (key, val) = line.split()
                self.my_dictionary[key] = val
                
        
    def getParam(self, myKey):
        '''
        returns the value of a key of the dictionary
        '''
        return self.my_dictionary[myKey]
    
