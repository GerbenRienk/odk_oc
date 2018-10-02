'''
Created on 20180818

@author: GerbenRienk
'''
from utils.dictfile import readDictFile
from utils.ocwebservices import studySubjectWS, studyEventWS, dataWS

def test_it():
    config=readDictFile('odkoc.config')

    # initialise the oc-webservice
    myWebService = studyEventWS(config['userName'], config['password'], config['baseUrl'])
    my_results = myWebService.scheduleEvent(config['studyIdentifier'], 'TDS005',config['studyEventOID'], 'def', '1980-01-01')
    print(my_results)
    
if __name__ == '__main__':
    test_it()
