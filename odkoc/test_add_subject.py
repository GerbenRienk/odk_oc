'''
Created on 20180818

@author: GerbenRienk
'''
from utils.dictfile import readDictFile
from utils.ocwebservices import studySubjectWS, dataWS

def test_it():
    config=readDictFile('odkoc.config')

    # initialise the oc-webservice
    myWebService = studySubjectWS(config['userName'], config['password'], config['baseUrl'])
    my_results = myWebService.addStudySubject('MA006','TDS002')
    print(my_results)
    
if __name__ == '__main__':
    test_it()
