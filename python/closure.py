#!/usr/bin/python
__author__ = "olenji"

class A:
    def here(self):
        data = "A.here"
        def inline(param):
            print(data)
            print(param)

        aB = B()
        aB.here(inline)

class B:
    def here(self, callbackfuc):
        data = "B.here"
        callbackfuc(data)

if __name__ == '__main__':
    aa = A()
    aa.here()
