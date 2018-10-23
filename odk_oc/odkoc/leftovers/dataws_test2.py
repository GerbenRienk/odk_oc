'''
Created on 9 apr. 2017

@author: GerbenRienk
'''

import requests
baseUrl = 'https://tds-edc.com/rdpws'

wsUrl = baseUrl + '/ws/data/v1/dataWsdl.wsdl'
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://openclinica.org/ws/data/v1" xmlns:bean="http://openclinica.org/ws/beans"><soapenv:Header>
 <wsse:Security soapenv:mustUnderstand="1" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
 <wsse:UsernameToken wsu:Id="UsernameToken-27777511" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
 <wsse:Username>grvisser</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">9db90f25218c6d8a0ba1c92cda4f98eba3ac8b47</wsse:Password>
 </wsse:UsernameToken>
 </wsse:Security>
</soapenv:Header><soapenv:Body>      <v1:importRequest>      <ODM><ClinicalData StudyOID="S_RDP001" MetaDataVersionOID="v1.0.0">
<SubjectData SubjectKey="SS_RDP002">
<StudyEventData StudyEventOID="SE_LS" >
<FormData FormOID="F_TDSCRFFORLIM_V1" >
<ItemGroupData ItemGroupOID="IG_TDSCR_UNGROUPED" TransactionType="Insert">
<ItemData ItemOID="I_TDSCR_LSDATA" Value="2"/>
</ItemGroupData>
</FormData>
</StudyEventData>
</SubjectData>
</ClinicalData>      </ODM>      </v1:importRequest></soapenv:Body></soapenv:Envelope>"""

response = requests.post(wsUrl,data=body,headers=headers)
print (response.content)



