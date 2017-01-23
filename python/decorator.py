#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "olenji"
import time

def bar(func):
    print "bar"
    return func

@bar
def foo():
    print "foo"

#foo()


print '=' * 40
def function_performance_statistics(trace_this=True):  
    if trace_this:  
       def performace_statistics_delegate(func):  
            def counter(*args, **kwargs):  
                start = time.clock()  
                func(*args, **kwargs)  
                end =time.clock()  
                print 'used time: %d' % (end - start, )  
            return counter  
    else:  
       def performace_statistics_delegate(func):  
            return func  
    return performace_statistics_delegate  
 
@function_performance_statistics(True)  
def add(x, y):  
    time.sleep(3)  
    print 'add result: %d' % (x + y,)  
 
@function_performance_statistics(False)  
def mul(x, y=1):  
    print 'mul result: %d' % (x * y,)  
  
add(1, 1)  
mul(10)

print '=' * 40

def aa(arg):
    print "here is aa "
    def a(f):
        print "here is a"
        def _a(*args, **kwargs):
            print "before %s" % arg
            res = f(*args, **kwargs)
            print locals()
    	    return res
        print locals()
        print "here is end a"
        return _a
    print locals()
    print "here id end aa"
    return a

def aaa(func):
    print "here is aaa"
    return func

@aaa
@aa("olenji")
def func(b):
    print "do something: like %s" % b
    print locals()

func("wash")

print '=' * 40




