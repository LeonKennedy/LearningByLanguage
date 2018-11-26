#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: LookingGlass.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: with的用法
# @Create: 2018-11-26 11:47:06
# @Last Modified: 2018-11-26 11:47:06
#

class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWCOKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])
    
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please Do Not dividle by z!')
            return True

if __name__ == "__main__":
    with LookingGlass() as what:
        print("Alice, Kitty and Snowdrop")
        print(what)
    print('Back to Normal')
