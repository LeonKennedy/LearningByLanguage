#!/usr/bin/python
#encoding=utf-8
'''
 author     : olenji
 date       : 2016-12-14 14:20:00
 function   : 图片操作
 py_version ：2.7.2
'''

from PIL import Image
from StringIO import StringIO
from identification import main

class Picture(object):
    
    img = None
    def __init__(self,source):
        self.img = Image.open(source)

    def cut(self):
        box = (659,20, 770,65)
        newimg = self.img.crop(box)
        newimg.save("/tmp/qcode.png",'png')


if __name__ == "__main__":
    f = open("temp_img", 'rb')
    a = f.read()
    f.close()
    i = Picture(StringIO(a))
    i.cut()
    f = open("/tmp/qcode.png", 'rb')
    b = f.read()
    f.close()
    main(b)

