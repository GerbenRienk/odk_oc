'''
Created on 3 mei 2017

@author: GerbenRienk
'''
import time
from datetime import datetime, timedelta

def TestSleep():
    
    param = "00:00:15"
    param_list = param.split(sep=':')
    max_difference = timedelta(hours=int(param_list[0]), minutes=int(param_list[1]), seconds=int(param_list[2]))
    start_time = datetime.now()
    while True:
        print('in loop', start_time)
        time.sleep(2)
        stop_time = datetime.now()
        print('after sleep', stop_time)
        difference = stop_time - start_time
        print('difference :', difference )
        #max_difference = datetime.timedelta(delta)
        if difference > max_difference:
            break
    print('***', start_time, stop_time)
    
if __name__ == '__main__':
    TestSleep()
