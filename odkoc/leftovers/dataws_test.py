'''
Created on 9 apr. 2017

@author: GerbenRienk
'''


import logging.config

_logger = logging.getLogger(__name__)
logging.config.fileConfig("logging.ini", disable_existing_loggers=False)

from dictfile import readDictFile
from ocwebservices import dataWS

config=readDictFile('oli.config')

print("start import oc data")
myDataWS = dataWS(config['userName'], config['password'], config['baseUrl'])
resultOfSubmit = myDataWS.submitData()





