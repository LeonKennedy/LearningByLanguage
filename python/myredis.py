#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: myredis.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: redis使用
# @Create: 2018-03-02 11:36:28
# @Last Modified: 2018-03-02 11:36:28
#

import redis
#CONFIG = configparser.ConfigParser()  
#CONFIG.read("config/system.ini")  
#redis_host = CONFIG.get("redis", "REDIS_HOST")  
#redis_port = CONFIG.get("redis","REDIS_PORT")  
#redis_db=CONFIG.get("redis","REDIS_DB")  
#redis_pwd=CONFIG.get("redis","REDIS_PASSWORD") 
redis_host = '127.0.0.1'
redis_port = 6379
redis_db=0
redis_pwd=None

redisConnect = redis.Redis(redis_host,redis_port,redis_db,redis_pwd)  
  
class RedisTool:  
 
    @staticmethod  
    def hexists(name,key):  
        return redisConnect.hexists(name,key)  
 
    @staticmethod  
    def hget(name, key):  
        return redisConnect.hget(name, key)  
 
    @staticmethod  
    def getset(name, value):  
        return redisConnect.getset(name, value)  
 
    @staticmethod  
    def hdel(name, *keys):  
        return redisConnect.hdel(name, *keys)  
 
    @staticmethod  
    def hgetall(name):  
        return redisConnect.hgetall(name)  
 
    @staticmethod  
    def hkeys(name):  
        return redisConnect.hkeys(name)  
 
    @staticmethod  
    def hlen(name):  
        return redisConnect.hlen(name)  
  
    #Set key to value within hash name Returns 1 if HSET created a new field, otherwise 0  
    @staticmethod  
    def hset(name, key, value):  
        return redisConnect.hset(name, key, value)  
 
    @staticmethod  
    def setex(name, time, value):  
        return redisConnect.setex(name, time, value)  
 
    @staticmethod  
    def get(name):  
        return redisConnect.get(name)  
 
    @staticmethod  
    def exists(name):  
        return redisConnect.exists(name)  
         
    @staticmethod  
    def set(name, value):  
        return redisConnect.set(name, value)


if __name__ == "__main__":
	RedisTool.set('a',1)
	
