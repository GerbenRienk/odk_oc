'''
Created on 20180818

@author: GerbenRienk
'''
from utils.dictfile import readDictFile
from utils.pg_api import ConnToOdkUtilDB, ConnToOdkDB, PGSubject
from utils.ocwebservices import studySubjectWS, studyEventWS, dataWS
from utils.ma006 import compose_reader

def test_it():
    config=readDictFile('odkoc.config')
    print('start')
    myDataWS = dataWS(config['userName'], config['password'], config['baseUrl'])
    conn_odk = ConnToOdkDB()
    conn_util = ConnToOdkUtilDB()
    odk_results = conn_odk.ReadDataFromOdkTable("odk_prod.\"HS_RDT_READER_1_V1_CORE\"")
    for odk_result in odk_results:
        study_subject_id = odk_result['GENERAL_INFORMATION_STUDY_SUBJECT_ID']
        study_subject_oid = conn_util.DLookup('study_subject_oid', 'study_subject_oc', 'study_subject_id=\'%s\'' % (study_subject_id))
        dummy = compose_reader(study_subject_oid, odk_result)
        
        import_results = myDataWS.importData(dummy)
        print(import_results)

    print('end')
    
if __name__ == '__main__':
    test_it()
