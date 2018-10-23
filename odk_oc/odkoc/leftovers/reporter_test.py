'''
Created on 9 mei 2017

@author: GerbenRienk
'''
from utils.reporter import Reporter

def DoIt():
    my_report = Reporter()
    log_line = 'yes'
    my_report.append_to_report(log_line)
    my_report.append_to_report('no')
    print('*')
    
if __name__ == '__main__':
    DoIt()