from ocwebservices import studySubjectWS
from dictfile import readDictFile

config=readDictFile('odkoc.config')
#myFile=filesOnDisk.propertiesFile('odkoc.config')

myWebService = studySubjectWS(config['userName'], config['password'], config['baseUrl'])

allStudySubjectEvents = myWebService.getListStudySubjectEvents(config['studyIdentifier'])
# now output the list of ListSeparator
for my_studysubject_event in allStudySubjectEvents:
    print(my_studysubject_event, "check ", my_studysubject_event[1])
    