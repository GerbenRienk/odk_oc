import hashlib

import zeep
from lxml import etree
from zeep.wsse import UsernameToken


# Logging
import logging
import logging.config

_logger = logging.getLogger(__name__)
#logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
           
class ocwsStudySubject(object):
    def __init__(self, username, password, wsUrl):
        passwordHash = hashlib.sha1(password.encode('utf-8')).hexdigest()

        self._client = zeep.Client(
            wsUrl,
            strict=False,
            wsse=UsernameToken(username, password=passwordHash))

    def get_studysubjects(self,identifier):
        """Get a list of study subject events

        """
        with self._client.options(raw_response=True):
            response = self._client.service.listAllByStudy({
                'identifier': identifier
                })
            if response.status_code != 200:
                return None

            #the response needs cleaning up
            document = str(response.content)
            document = document[document.index('<SOAP'):]
            document = document[0:document.index('</SOAP-ENV:Envelope>') + 20]
            
            xml_output = etree.fromstring(document)
            relevant_part = xml_output.xpath('//ns4:studySubjects', namespaces={
                'ns2': 'http://openclinica.org/ws/beans', 'ns4': 'http://openclinica.org/ws/studySubject/v1'
            })
            return relevant_part

#initiate the webservice client            
client=ocwsStudySubject('grvisser', 'Ged30gra', 'https://tds-edc.com/rdpws/ws/study/v1/studySubjectWsdl.wsdl')

for all_subjects in client.get_studysubjects('RDP001'):    
    #initialise a list to return
    all_studysubject_events = []
    for one_subject in all_subjects.xpath('//ns2:studySubject', namespaces={'ns2': 'http://openclinica.org/ws/beans'}):
        for one_subject_infoblocks in one_subject.getchildren():
            #is this the label?
            if one_subject_infoblocks.tag == '{http://openclinica.org/ws/beans}label':
                studySubjectID = one_subject_infoblocks.text
            if one_subject_infoblocks.tag == '{http://openclinica.org/ws/beans}events':
                for all_events in one_subject_infoblocks.getchildren():
                    for one_event_info in all_events.getchildren():
                        if one_event_info.tag == '{http://openclinica.org/ws/beans}eventDefinitionOID':
                            eventDefinitionOID = one_event_info.text
                        if one_event_info.tag == '{http://openclinica.org/ws/beans}startDate':
                            startDate = one_event_info.text
                    
                    one_studysubject_event = studySubjectID,eventDefinitionOID,startDate
                    all_studysubject_events.append(one_studysubject_event)

# now output the list of ListSeparator
for my_studysubject_event in all_studysubject_events:
    print(my_studysubject_event, "check ", my_studysubject_event[1])
    
    