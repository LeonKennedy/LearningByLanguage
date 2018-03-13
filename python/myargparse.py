#!/usr/bin/python
#encoding=utf-8
'''
 author     : olenji
 date       : 2016-12-14 14:20:00
 function   : 图片操作
 py_version ：2.7.2
'''

from PIL import Image

import argparse  
  
#### 参数调用说明  
parser = argparse.ArgumentParser()  
parser.add_argument('-t','--tcp', help='tcp service',action='store_true')  
parser.add_argument('-u', '--udp', help='udp service', action='store_true')  
parser.add_argument('-s', '--scheduler', help='one of rr|wrr|lc|wlc|lblc|lblcr|dh|sh|sed|nq,the default scheduler is wlc')  
parser.add_argument('-p', '--persistent', help='persistent service, default:1500', type = int)  
parser.add_argument('-r', '--realserver', help="server-address is host (and port) Example: -r '1.1.1.1 2.2.2.2 3.3.3.3'", type = str )  
parser.add_argument('-f', '--floapingip', help='vip address of lvs' )  
parser.add_argument('-g', '--gatewaying', help='gatewaying (direct routing)',action='store_true')  
parser.add_argument('-m','--masquerading', help='masquerading (NAT)', action='store_true')  
parser.add_argument('-S','--srcport', help='listen on floapip port', type = int )  
parser.add_argument('-R','--destport', help='listen on realserver port', type = int )  
args = parser.parse_args()  

#action='store_true' 表明该参数不接受参数传递， 即， 只接受 -t 或 --tcp 下面是错误例子 -t tcp  或 --tcp=yes  
#假如需要接受参数， 如 -t tcp 或 --tcp=yes 那么不可以使用 action 进行定义  
#假如需定义参数传入格式， 可使用 type = int|str|complax 进行定义  


#假如执行过程中， 调用参数 -S 80 或 --srcport=80  传递  
#args.srcport = 80 

#执行时可能存在多个空格  
#/app.py --realserver="1.1.1.1 2.2.2.2   3.3.3.3       4.4.4.4"  
#realip =  re.sub(r'\s+', ' ',args.realserver)  
#realip 格式变成 1.1.1.1 2.2.2.2 3.3.3.3 4.4.4.4 只存在一个空格分隔符
