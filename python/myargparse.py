#!/usr/bin/python
# encoding=utf-8
'''
 author     : coffee
 date       : 2016-12-14 14:20:00
 function   : argsparse
 py_version ：3.8
'''

import argparse


def init_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--scheduler',
                        help='one of rr|wrr|lc|wlc|lblc|lblcr|dh|sh|sed|nq,the default scheduler is wlc')
    parser.add_argument('-p', '--persistent', help='persistent service, default:1500', type=int)
    parser.add_argument('-r', '--realserver',
                        help="server-address is host (and port) Example: -r '1.1.1.1 2.2.2.2 3.3.3.3'", type=str)
    parser.add_argument('-f', '--floapingip', help='vip address of lvs')
    parser.add_argument('-g', '--gatewaying', help='gatewaying (direct routing)', action='store_true')
    parser.add_argument('-m', '--masquerading', help='masquerading (NAT)', action='store_true')
    parser.add_argument('-S', '--srcport', help='listen on floapip port', type=int)
    parser.add_argument('-R', '--destport', help='listen on realserver port', type=int)

    return args


# 互斥
def exp_mutually(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--tcp', help='tcp service', action='store_true')  # default false
    group.add_argument('-u', '--udp', help='udp service', action='store_true')
    args = parser.parse_args()
    print("tcp: ", args.tcp, "udp:", args.udp)


def exp1(parser):
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    print(args.accumulate(args.integers))


# MetavarTypeHelpFormatter 使用类型作为metavar
def exp2(parser):
    parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('--foo', type=int, required=True)
    parser.add_argument('bar', type=float)
    args = parser.parse_args()
    print(args.bar, args.foo)


def exp3(parser):
    parser.add_argument("--foo", action="extend", nargs="+", type=str)
    print(parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"]))
    parser.add_argument('--verbose', '-v', action='count', default=0)
    print(parser.parse_args(['-vvv']))

def exp4(parser):
    parser.add_argument('--foo', nargs='?', const='c', default='d')
    parser.add_argument('bar', nargs='?', default='d')
    print(parser.parse_args(['XX', '--foo', 'YY']))
    print(parser.parse_args(['XX', '--foo']))
    print(parser.parse_args([]))

# 假如需定义参数传入格式， 可使用 type = int|str|complax 进行定义


# 执行时可能存在多个空格
# /app.py --realserver="1.1.1.1 2.2.2.2   3.3.3.3   4.4.4.4"
# realip =  re.sub(r'\s+', ' ',args.realserver)
# realip 格式变成 1.1.1.1 2.2.2.2 3.3.3.3 4.4.4.4 只存在一个空格分隔符

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    exp4(parser)
