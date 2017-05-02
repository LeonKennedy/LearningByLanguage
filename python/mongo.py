#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: mongo.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: --- 测试mongoDB的小例子
# @Create: 2017-05-02 16:43:06
# @Last Modified: 2017-05-02 16:43:06
#

from datetime import datetime
from pymongo import MongoClient
import pdb

if __name__ == "__main__":
    client = MongoClient()
    db = client.play

    content = { "address": {
               "street": "2 Avenue", "zipcode": "10075", "building": "1480",
               "coord": [-73.9557413, 40.7720266] },
               "borough": "Manhattan", "cuisine": "Italian", 
               "grades": [ { "date": datetime.strptime("2014-10-01", "%Y-%m-%d"), "grade": "A", "score": 11 }, 
               { "date": datetime.strptime("2014-01-16", "%Y-%m-%d"), "grade": "B", "score": 17 } ], 
               "name": "Vella", "restaurant_id": "41704620" }
    result = db.t1.insert_one(content)
    print(result.inserted_id)

