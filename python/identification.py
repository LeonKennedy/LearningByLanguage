#!/usr/bin/python
#encoding=utf-8
'''
 author     : olenji
 date       : 2016-12-12 14:20:00
 function   : 识别验证码使用
               其实还是调用别人api
 py_version ：2.7.2
'''

import urllib2
import time, json

def main(raw_img):
 
    submitUrl = 'http://op.juhe.cn/vercode/index' #接口地址
    appkey = '8539a23dcd33461b81f13e8a7118fbe5' #接口申请的key
    codeType = '1004' #验证码的类型
    imagePath = 'hhh' #图片本地地址
 
    #buld post body data
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
 
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'key')
    data.append(appkey)
    data.append('--%s' % boundary)
 
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'codeType')
    data.append(codeType)
    data.append('--%s' % boundary)
 
    data.append('Content-Disposition: form-data; name="%s"; filename="b.png"' % 'image')
    data.append('Content-Type: %s\r\n' % 'image/png')
    data.append(raw_img)
    data.append('--%s--\r\n' % boundary)
 
    http_body='\r\n'.join(data)
    try:
        req=urllib2.Request(submitUrl, data=http_body)
 
        #header
        req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
        req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36')
        req.add_header('Referer','http://op.juhe.cn/')
 
        resp = urllib2.urlopen(req, timeout=30)
 
        qrcont=resp.read()
 
        result = json.loads(qrcont, 'utf-8')
        error_code = result['error_code']
        if(error_code == 0):
            data = result['result'] #接口返回结果数据
            print(data)
            return data
        else:
            errorinfo = u"错误码:%s,描述:%s" % (result['error_code'],result['reason']) #返回不成功，错误码:原因
            print(errorinfo)
 
    except Exception,e:
       print e.args
 

def imgfromurl(url):
    f = urllib2.urlopen(url)
    raw_data = f.read()
    f.close()
    return  main(raw_data)

def imgfromfile():
    imagePath = 'hhh' #图片本地地址
    fr = open(imagePath, 'rb')
    raw_data = fr.read()
    fr.close()
    return  main(raw_data)
if __name__ == "__main__":
    url = 'http://mp.weixin.qq.com/mp/verifycode?cert=1481523753475.1445'
    imgfromurl(url)
