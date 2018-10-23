'''
Created on 16 apr. 2017

@author: GerbenRienk
'''
class StudySubject(object):
    '''to get the study subject oid from the study subject id
    by calling the rest-webservice
    Only parameter is study subject id
    Connection info is read from oli.config
    '''
    def __init__(self, StudySubjectID):
        self._studysubjectid = StudySubjectID
        return
    
    def GetSSOID(self):
        'method to get the study subject oid'
        import requests
        import xml.etree.ElementTree as ET
        from utils.dictfile import readDictFile
        config=readDictFile('oli.config')
        
        login_url = config['baseUrlRest'] + '/j_spring_security_check'
        login_action = {'action':'submit'}
        login_payload = {
            'j_username': config['userName'],
            'j_password': config['password'],
            'submit':"Login"
                        }
        mySession = requests.Session()
        mySession.post(login_url,params=login_action,data=login_payload)
        cd_url = config['baseUrlRest'] + '/rest/clinicaldata/xml/view/' + config['studyOid'] + '/'
        cd_url = cd_url + self._studysubjectid + '/*/*'
        clinical_data = mySession.get(cd_url)
        
        document = clinical_data.content
        root = ET.fromstring(document)
                    
        for cd in root.findall('{http://www.cdisc.org/ns/odm/v1.3}ClinicalData/'):
            sinfo = cd.attrib
            if sinfo['{http://www.openclinica.org/ns/odm_ext_v130/v3.1}StudySubjectID'] == self._studysubjectid:
                return sinfo['SubjectKey']

def main():
    print('test me')
    ssoid = StudySubject('RDP001').GetSSOID()
    print(ssoid)

if __name__ == '__main__':
    main()