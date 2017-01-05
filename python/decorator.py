#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "olenji"


def aa(arg):
    def a(f):
        def _a(*args, **kwargs):
            print "before %s" % arg
            res = f(*args, **kwargs)
            print "after"
    	    return res
        return _a
    return a

@aa("olenji")
def func(b):
    print "do something: like %s" % b

func("wash")
