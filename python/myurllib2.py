#!/usr/bin/env python
# -*- coding: utf-8 -*-
#***********************************************
#
#      Filename: myurllib2.py
#
#        Author: olenji - lionhe0119@hotmail.com
#   Description: ---
#        Create: 2017-03-03 10:16:29
# Last Modified: 2017-03-03 10:16:29
#**********************************************/


import urllib2,cookielib,time, json

cj = cookielib.LWPCookieJar() 
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# 将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

response_param= {'skey':'@crypt_fc7a3860_d0e82e64da30bfbfd79542b87d457fe7','wxsid':'Qt28jzqEyMcCUPw7','wxuin':'417123915','pass_ticket':'4Lp3ixXHsV49sv6BKbSKcb%2BWlM8Zszq2vYDIxpf8YJ2nDPurvoQwhxwhHup0jvY8'}
url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=%s&lang=zh_CN&pass_ticket=%s' % (int(time.time()), response_param['pass_ticket'])
postdata={'BaseRequest':{}}
postdata['BaseRequest']['Uin'] = response_param['wxuin']
postdata['BaseRequest']['Sid'] = response_param['wxsid']
postdata['BaseRequest']['Skey'] = response_param['skey']
postdata['BaseRequest']['Skey'] = response_param['skey']
postdata['BaseRequest']['DeviceID'] = response_param['pass_ticket']
headers = {'ContentType':'application/json; charset=UTF-8'}
req = urllib2.Request(url=url, data=json.dumps(postdata), headers=headers)
result = urllib2.urlopen(req)
page = result.read()
print page
