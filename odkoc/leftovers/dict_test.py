'''
Created on 5 mei 2017

@author: GerbenRienk
'''
class Reporter(object):
    def __init__(self):
        pass

    
    def DoIt(self):
        print('start')
        file = open('logs/testfile.txt','w') 
        file.write('hw')
        print('end')
        return None
        
        
    if __name__ == '__main__':
        pass