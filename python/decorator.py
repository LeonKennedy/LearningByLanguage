#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "olenji"
import functools
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%.8fs] %s(%s) -> %r' % (elapsed, func.__name__, arg_str, result))
        return result

    return clocked


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


factorial(6)
print('function factorial name: %s' % factorial.__name__)
print('upgrade clock with functools.wrap')


def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs_items())]
            arg_lst.append(pairs)
        arg_str = ', '.join(arg_lst)
        print('[%.8fs] %s(%s) -> %r' % (elapsed, func.__name__, arg_str, result))
        return result

    return clocked


@clock2
def factorial2(n):
    return 1 if n < 2 else n * factorial2(n - 1)


factorial2(6)
# 所以一般写装饰器用functools.wrap 它会把很多事处理好
print('function factorial2 name: %s' % factorial2.__name__)

print('=' * 40)


# 带参数的装饰器 是要多加一层装饰器工厂 用来接受参数
def function_performance_statistics(trace_this=True):
    if trace_this:
        def performace_statistics_delegate(func):
            def counter(*args, **kwargs):
                start = time.clock()
                func(*args, **kwargs)
                end = time.clock()
                print('used time: %d' % (end - start,))

            return counter
    else:
        def performace_statistics_delegate(func):
            return func
    return performace_statistics_delegate


@function_performance_statistics(True)
def add(x, y):
    time.sleep(3)
    print('add result: %d' % (x + y,))


@function_performance_statistics(False)
def mul(x, y=1):
    print('mul result: %d' % (x * y,))


add(1, 1)
mul(10)

print('=' * 40)


def aa(arg):
    print("here is aa ")

    def a(f):
        print("here is a")

        def _a(*args, **kwargs):
            print("before %s" % arg)
            res = f(*args, **kwargs)
            print(locals())
            return res

        print(locals())
        print("here is end a")
        return _a

    print(locals())
    print("here id end aa")
    return a


def aaa(func):
    print("here is aaa")
    return func


@aaa
@aa("olenji")
def func(b):
    print("do something: like %s" % b)
    print(locals())


func("wash")

print('=' * 40)
