#encoding:utf-8

'''
 author     : olenji
 date       : 2016-11-8 14:20:00
 function   : BeautifulSoup的小李子
 py_version ：2.7.2
'''

from bs4 import BeautifulSoup

class BSProcess(object):
    
    @staticmethod
    def simplify(data):
        bs = BeautifulSoup(data, 'lxml')
        print dir(bs)
        print bs.get_text()
