#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: mycrypto.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: 使用AES解密
# @Create: 2018-09-28 14:09:26
# @Last Modified: 2018-09-28 14:09:26
#

import base64, pdb
from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex


def Encrypt(key, iv, instr):
    mystr = _pad(instr)
    cipher = AES.new(key, AES.MODE_ECB)
    #ret = base64.b64encode(cipher.encrypt(mystr))
    ret = cipher.encrypt(mystr)
    return ret

def Decrypt(key, iv, encryptedData):
    #encryptedData = base64.b64decode(encryptedData)
    #encryptedData = bytes(encryptedData, encoding='utf8')
    cipher = AES.new(key, AES.MODE_ECB)
    c = cipher.decrypt(encryptedData)
    ret = c.decode(encoding="utf-8", errors = 'ignore' )
    ret = _unpad(ret)
    return ret

def _pad(s):
    BS = AES.block_size
    s = s.encode("utf-8")
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode("utf-8")

def _unpad(s):
    return s[:-ord(s[len(s)-1:])]

def main():
    #with open('encrypt_data.txt', 'r', encoding='utf-8') as fp:
    #  s = fp.read()
    #s = s[:-1]
    #s = base64.b64decode(s)
    encryptedData = b'\xb6[(0/N\x12C\x00\xca\xf0\xf10\x93<\xdf'
    mystr = '合肥'
    key = 'bojgeveoi\0\0\0\0\0\0\0'
    iv =  '0000000000000000'

    print(Encrypt(key, iv, mystr))
    print(Decrypt(key, iv, encryptedData))
    #print(Decrypt(key,iv ,s))

if __name__ == '__main__':
    main()

