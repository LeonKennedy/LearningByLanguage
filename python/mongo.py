#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @ilename: mongo.py
# @Author olenji - lionhe0119@hotmail.com
# @Description: --- 测试mongoDB的小例子
# @Create: 2017-05-02 16:43:06
# @Last Modified: 2017-05-02 16:43:06
#

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

from datetime import datetime
from pymongo import MongoClient
import pdb, logging, json

logging.basicConfig(level=logging.INFO)
class mangguoDB:
    def __init__(self):
        uri = "mongodb://%s:%s@%s/taobao" % (
            "kst", "kst410", "121.40.107.148:27017")
        self.client = MongoClient(uri)
        self.goods_list = list()
        self.insertCount = 0

    def query(self, table=None, collection=None):
        db = self.client[table]
        result = db[collection].find().skip(1).limit(1)
        for i in result:
            item = dict(i)
            self.goods_list.apend(item['goods_id'])
            ask_list = item['ask_around_list']
            for ask in ask_list:
                print(ask)

    def update(self):
        pass

    def delete(self):
        pass

    # ---------------- 业务相关  ----------
    def taobaoSpiltAsk(self):
        db = self.client.taobao
        commondb = self.client.common
        limit = 10
        skip = 0
        insertCount = 0
        result = db.ask_around.find().skip(skip).limit(limit)
        for i in result:
            item = dict(i)
            tbitem = dict()
            tbitem['url'] = item['goods_url']
            tbitem['price'] = item['price']
            tbitem['content'] = item['goods_name']
            tbitem['location'] = item['local']
            tbitem['shop_id'] = item['shop_id']
            tbitem['item_id'] = item['goods_id']
            tbitem['category_id'] = item['category_id']

            ask_list = item['ask_around_list']
            for ask in ask_list:
                a = commondb.ask.find_one({'topic_id' : ask['topic_id']})
                if not a:
                    commondb.ask.insert_one(ask)
                    self.insertCount += 1
                    insertCount += 1
        logging.info("from %d  insert %d item" % (skip,insertCount))
        skip += limit

    def yhdExtract(self):
        db = self.client.yhd
        commondb = self.client.common
        limit = 10000
        skip = 0
        while 1:
            insertCount = 0
            result = db.ask.find().skip(skip).limit(limit) 
            for i in result:
                item = dict(i)
                ask = dict()
                ask['ask_time'] = item['question_tm']
                ask['question'] = item['question']
                ask['question_user'] = item['question_user']
                ask['origin'] = 'yhd'
                ask['answer_list'] = [{'answer':item['answer'], 'answer_user':item['answer_user'], 'answer_time':item['answer_tm']},]
                commondb.ask_yhd.insert_one(ask)
                insertCount += 1
                self.insertCount += 1
            logging.info("from %d  insert %d item" % (skip,insertCount))
            if insertCount == 0 :
                return True
            skip += limit


    def test(self):
        db = self.client.play
        content = { "address": {
               "street": "2 Avenue", "zipcode": "10075", "building": "1480",
               "coord": [-73.9557413, 40.7720266] },
               "borough": "Manhattan", "cuisine": "Italian", 
               "grades": [ { "date": datetime.strptime("2014-10-01", "%Y-%m-%d"), "grade": "A", "score": 11 }, 
               { "date": datetime.strptime("2014-01-16", "%Y-%m-%d"), "grade": "B", "score": 17 } ], 
               "name": "Vella", "restaurant_id": "41704620" }
        result = db.t1.insert_one(content)
        print(result.inserted_id)

        
    def __del__(self):
        logging.info("[END] total insert %d record" % self.insertCount)
        pass

if __name__ == "__main__":
    a = mangguoDB()
    a.test()
    #a.query('taobao', 'ask_around')
    #a.taobaoSpiltAsk()
    #a.yhdExtract()

