#!/usr/bin/python
# encoding=utf-8
# ***********************************************
#
#      Filename: turingrobot.py
#
#        Author: olenji - lionhe0119@hotmail.com
#   Description: turing robot of chat
#        Create: 2017-01-10 22:59:11
# Last Modified: 2017-01-10 22:59:11
# ***********************************************/

import json
import requests


class ChatRobot(object):

    def chat(self, text):
        apikey = "b85870a566c94f2c895c149f6fda16c7"
        url = "http://www.tuling123.com/openapi/api"
        body = {
            "key": apikey,
            "info": text
        }
        rep = requests.post(url, json.dumps(body))
        jtext = json.loads(rep.content)
        return jtext['text']


if __name__ == "__main__":
    a = ChatRobot()
    print(a.chat("你好"))
    print(a.chat("你真的好傻"))

