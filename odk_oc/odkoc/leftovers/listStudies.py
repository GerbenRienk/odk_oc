import hashlib

import zeep
from lxml import etree
from zeep.wsse import UsernameToken

# Logging
#import logging
import logging.config

_logger = logging.getLogger(__name__)
logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
 

class ocwsStudy(object):
    def __init__(self, username, password, wsUrl):
        passwordHash = hashlib.sha1(password.encode('utf-8')).hexdigest()

        self._client = zeep.Client(
            wsUrl,
            strict=False,
            wsse=UsernameToken(username, password=passwordHash))

    def get_studies(self):
        """Generator which yields a dict containing the study, site and
        metadata.

        """
        #get the result to return
        result = self._client.service.listAll()
        #add the metadata to each study/site
        for study in result.studies.study:
            for site in study.sites.site:
                metadata = self.study_metadata(site.identifier)
                yield {
                    'study': study,
                    'site': site,
                    'metadata': metadata
                }
            
    def study_metadata(self, identifier):
        """Retrieve the getMetadata for a study.

        Note that the WSDL doesn't match the data returned by the SOAP server
        so we let zeep return the raw requests response and extract the
        odm node ourselves.

        :param identifier: The study identifier
        :return: The ODM document
        :rtype: lxml.etree._Element

        """
        with self._client.options(raw_response=True):
            response = self._client.service.getMetadata({
                'identifier': identifier
            })

            if response.status_code != 200:
                return None

            
            document = etree.fromstring(response.content)
            odm = document.xpath('//ns:odm', namespaces={
                'ns': 'http://openclinica.org/ws/study/v1'
            })
            if odm:
                odm_string = odm[0].text.encode('utf-8')
                return etree.fromstring(odm_string)

client = ocwsStudy('grvisser', 'Ged30gra', 'https://tds-edc.com/rdpws/ws/study/v1/studyWsdl.wsdl')

for myStudy in client.get_studies():
    myStudyInfo = myStudy.get('study')
    print(myStudyInfo.identifier)
    #print('Study: ',myStudy['study'])
    #print('Site: ', study['site'])
    #print('Metadata:')
    #print(etree.tostring(study['metadata'], pretty_print=True).decode('utf-8'))

