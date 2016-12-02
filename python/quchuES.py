#encoding:utf-8

'''
 author     : olenji
 date       : 2016-11-30 16:00:00
 function   : 1.创建需要的quchu elasticsearch 需要的 index
 py_version ：2.7.2
'''

from datetime import datetime
from elasticsearch import Elasticsearch
import requests, json

class QuchuElastic(object):

    es = doc_type = doc_index = None
    def __init__(self, h, p):
        self.baseurl = "http://%s:%d" % (h,p)
        self.es = Elasticsearch(host = h, port = p)
        self.bf = BodyFactory()
    
    def setIndex(self,index):
        self.doc_index = index

    #Index作用
    def index(self, body, doc_id = None, doc_type = None, doc_index=None):
        if not doc_index:
            if self.doc_index:
                doc_index = self.doc_index
            else:
                raise NameError("Please set index param...")
        if not doc_type:
            if self.doc_type:
                doc_type = self.doc_type
            else:
                raise NameError("Please set type param...")
        if doc_id:
            rep = self.es.index(index=doc_index, doc_type=doc_type, id = doc_id, body = body)
            print rep
        else:
            url = self.baseurl + "/%s/%s/" % (doc_index,doc_type)
            rep = requests.post(url, data=json.dumps(body))
            print(rep.content)
        return rep

    #文档不存在 则创建 返回201
    #文档存在 不创建 返回409
    def create(self, body, doc_id, doc_type = None, doc_index= None):
        if not doc_index:
            if self.doc_index:
                doc_index = self.doc_index
            else:
                raise NameError("Please set index param...")
        if not doc_type:
            if self.doc_type:
                doc_type = self.doc_type
            else:
                raise NameError("Please set type param...")
        url = self.baseurl + "/%s/%s/%s/_create" % (doc_index, doc_type, str(doc_id))
        rep = requests.post(url, data=json.dumps(body))
        print(rep.content)
        return rep

    #删除节点
    def deleteIndex(self, index):
        rep = self.es.indices.delete(index=index)
        print rep
        return rep['acknowledged']

    #存在并删除返回200   不存在返回404
    def delete(self, doc_index, doc_type, doc_id):
        url = self.baseurl + "/%s/%s/%s" % (doc_index, doc_type, str(doc_id))
        rep = requests.delete(url)
        print rep.content
        return rep

    #================ 更新 =====================
    #局部更新 将新的数据添加或者更新
    def update(self, doc_index, doc_type, doc_id):
        url = self.baseurl + "/%s/%s/%s/_update" % (doc_index, doc_type, str(doc_id))
        rep = requests.post(url)
        print rep.content
        return rep

    '''
    两个脚本类型更新的例子 一目了然
    GET /[index]/[type]/[id]/_update
    {
        "script" : "ctx._source.views += 1"
    }
    
    GET /[index]/[type]/[id]/_update
    {
        "script" : "ctx._source.tags += new_tags",
        "params":{
            "new_tags" : "search"
        }
    }
    
    '''

    # =====================  系统级别==============

    # 查看节点
    def nodes(self):
        req = requests.get(self.baseurl + "/_cat/nodes?v")
        print req.content

    # 查看ES状态
    def health(self):
        req = requests.get(self.baseurl + "/_cat/health?v")
        print req.content

    # 查看所有index
    def catIndices(self):
        req = requests.get(self.baseurl + "/_cat/indices?v")
        print req.content
        

    def matchall(self, index, doc_type = None):
        url = self.baseurl + "/%s/_search" % (index)
        body = {
            "query":{"match_all": {}}
        }
        req = requests.get(url, data=json.dumps(body))
        print req.content
        return req
    # 查看指定内容 
    def get(self,id):
        url = self.baseurl + "/%s/%s/%s" % (self.doc_index, self.doc_type, str(id))

    #根据关键字搜索
    def search_by_key(self, keys):
        url = self.baseurl + "/%s/%s/_search?pretty" % (self.doc_index, self.doc_type)
        body = {
            'query': {
                'match': {'content': keys}
            },
            '_source': [ 'name']
        }
        req = requests.get(url, data = json.dumps(body))
        #print req.content
        return req

    def base_search(self, doc_index, doc_type, body):
        url = self.baseurl + "/%s/%s/_search?pretty" % (doc_index, doc_type)
        req = requests.get(url, data = json.dumps(body))
        print req.content
        return req

    def wechat_search(self, key):
        body = {
            'query': {
                'match': {'content': key}
            },
            '_source': [ 'name']
        }
	self.base_search("wechat", "wechat_topic", body)

    def into_search(self, key):
	body = {
	    'query': {  
		'match' : {'shop_name': key}
	    },
	    'size' : 1
	}
	self.base_search("scrapingdb", "sjs_intoapp", body)

    def enjoy_search(self, key):
	body = {
  	    'query' : {
	#	'match_all' : {}
		'match' : {'shop_name' : key},
		'match' : {'product_description': key}
	    },
	    'size':10
	}
	self.base_search("scrapingdb", "sjs_enjoyapp", body)

    def xiancheng_search(self, key):
	body = {
  	    'query' : {
		'match_all' : {}
	    },
	    'size':3
	}
	self.base_search("scrapingdb", "sjs_xiancheng", body)

    #---------------分析--------------
    def analyzer(self, words):
        url =  self.baseurl + '/_analyze'
        params = {'analyzer': 'smartcn', 'pretty' : True , 'text' : words}
        req =  requests.get(url, params = params)
        print req.content
        return req

    def analyzer_with_index(self,word, doc_index):
        pass
    
    
    # 需要进一步包装的接口
    def _uncoverMethod(self):
        self.es.indices.create(index= 'test-index', ignore=[400,404])
        

    #------------------处理--------------------
    def handle(self, data):
        records = json.loads(data.content)
        result = []
        for art in records['hits']['hits']:
            result.append((art['_id'],art['_source']['name']))
        return result

    #处理一下关联
    #product
    def one(self, key):
        res = self.search_by_key(key)
        return self.handle(res)
        
    def test_requests(self):
        url = self.baseurl + "/%s/%s/_search?pretty" % (self.doc_index, self.doc_type)
        req = requests.get(url)
        print req.content
        print dir(req)
    
    #------------------- 配置 ------------------------
    def setall(self, doc_index):
        self.scrapingdb_setting(doc_index)
        self.type_xiancheng(doc_index)
        self.type_into(doc_index)
        self.type_enjoy(doc_index)
        self.type_yhouse(doc_index)
        self.type_topic(doc_index)

    def scrapingdb_setting(self, doc_index):
        url = self.baseurl + "/%s" % doc_index
        body={
            "settings":{
                "index" : {
                    "number_of_shards" : 1,
                    "number_of_replicas":0
                },
                "analysis": {
                    "analyzer":{
                        "htmlsmartcn":{
                            "tokenizer" : "smartcn_tokenizer",
                            "char_filter" : ['html_strip']
                        }     
                    }
                }

            }
        }
        req = requests.put(url, data=json.dumps(body))
        print req.content
        return req

    def type_enjoy(self, doc_index):
        doc_type = "sjs_enjoy"
        url = self.baseurl + "/%s/%s/_mapping" % (doc_index, doc_type)
        fieldtype = {"id":"int", "city":"not_analyzed", "area":"not_analyzed", "category": "not_analyzed", "subcategory": "not_analyzed", "product_id": "int",\
            "product_name":"smartcn" ,"product_short_name" : "smartcn" , "origin_price" : "int" , "price" : "int" , "product_type": "short", "refund_type":"short" , \
            "sell_begin_time":"no","sell_end_time":"no", "sell_state" : "no", "show_entity_name" : "no", "product_specification" : "no", "product_images" : "no", \
            "sub_product_id" : "int", "product_description" : "smartcn", "product_content" : "smartcn", "shop_id" : "int", "shop_name" : "smartcn", "shop_address" : \
            "smartcn", "latitude" : "float", "longtitude" : "float", "business_time" : "no", "shop_price_number" : "no", "phone_number" : "no", "shop_state" : "short"}
        req  =  requests.put(url, data= self.bf.createbodyjson(doc_type,fieldtype) )
        print req.content
        return req

    def type_into(self, doc_index):
        doc_type = "sjs_intoapp"
        url = self.baseurl + "/%s/%s/_mapping" % (doc_index, doc_type)
        fieldtype = {"item_id" : "int", "title" : "smartcn", "shop_id" : "int", "shop_name" : "smartcn", "shop_address" : "smartcn", "phone" : "no", "city" : "not_analyzed",\
            "item_hours" : "no", "price_list" : "not_analyzed", "help_tags" : "not_analyzed", "show_tags" : "smartcn", "show_end_tips" : "no", "map_longitude" : "float",   \
            "map_lattitude" : "float", "shop_image" : "no", "shop_hours" : "no", "shop_cost" : "int", "shop_tips" : "no", "shop_website" : "no", "zone" : "not_analyzed",   \
            "district" : "not_analyzed", "share_url" : "no", "like_precent" : "no", "have_coupon" : "no", "coupon_id" : "no", "coupon_title" : "no", "coupon_short_desc" :  \
            "no", "coupon_detail" : "no", "hot_num" : "short", "time_string" : "no", "time2_string" : "no", "cost_currency" : "no", "save_topic_rows" : "smartcn", "images" :\
            "no", "deal_rows" : "no", "review_rows" : "smartcn", "other_params" : "no", "current_shop" : "no" }
        req  =  requests.put(url, data= self.bf.createbodyjson(doc_type,fieldtype) )
        print req.content
        return req

    def type_yhouse(self, doc_index):
        doc_type = "sjs_yhouse"
        url = self.baseurl + "/%s/%s/_mapping" % (doc_index, doc_type)
        fieldtype = {"id" : "int", "product_id" : "int", "product_type" : "short", "product_details" : "smartcn", "city" : "not_analyzed", "district" : "not_analyzed", \
            "host_id" : "short", "host_name" : "smartcn", "host_address" : "smartcn", "latitude" : "float", "longitude" : "float", "host_details" : "no" }
        req  =  requests.put(url, data= self.bf.createbodyjson(doc_type,fieldtype) )
        print req.content
        return req

    #---wechat_topic---
    def type_topic(self, doc_index):
        doc_type = "wechat_topic"
        url = self.baseurl + "/%s/%s/_mapping" % (doc_index, doc_type)
        fieldtype = {"id" : "int", "uniqueid" : "not_analyzed", "url" : "no", "avatar" : "no", "title" : "smartcn", "abstract" : "smartcn", "content" : "htmlsmartcn", \
            "publish_time" : "date" , "create_time" : "date",  "wechat_id" : "int", "url_perm" : "no"}
        req  =  requests.put(url, data= self.bf.createbodyjson(doc_type,fieldtype) )
        print req.content
        return req

    def type_xiancheng(self, doc_index ):
        doc_type = "sjs_xiancheng"
        url = self.baseurl + "/%s/%s/_mapping" % (doc_index, doc_type)
        body = {
            doc_type: {
                "_all" : {"analyzer" : "smartcn"},
                "properties":{
                    "article_id" : {
                        "type" : "integer",
                        "index" : "no"
                    },
                    "article_title" : {
                        "type" : "text",
                        "analyzer" : "smartcn"
                    },
                    "city" : {
                        "type" : "text",
                        "index" : "not_analyzed"
                    },
                    "category" : {
                        "type" : "text",
                        "index" : "not_analyzed"
                    },
                    "article_publish_time" : {
                        "type" : "date"
                    },
                    "article_view_count" : {
                        "type" : "text",
                        "index" : "not_analyzed"
                    },
                    "article_author" : {
                        "type" : "text",
                        "index" : "not_analyzed"
                    },
                    "article_detail" : {
                        "type" : "text",
                        "index" : "not_analyzed"
                    },
                    "reason" : {
                        "type" : "text",
                        "analyzer" : "smartcn"
                    },
                    "shop_name" : {
                        "type" : "text",
                        "analyzer" : "smartcn"
                    },
                    "shop_address" : {
                        "type" : "text",
                        "analyzer" : "smartcn"
                    },
                    "shop_open_hours" : {
                        "type" : "text",
                        "index" : "no"
                    },
                    "shop_price" : {
                        "type" : "text",
                        "index" : "not_analyzed"
                    },
                    "shop_contact" : {
                        "type" : "text",
                        "index" : "not_analyzed"
                    },
                    "img_list" : {
                        "type" : "text",
                        "index" : "no"
                    },
                    "html" : {
                        "type" : "text",
                        "analyzer" : "htmlsmartcn",
                        "include_in_all" : True
                    }
                }
            }
        }
        req =  requests.put(url, data = json.dumps(body))
        print req.content
        return req

class BodyFactory(object):

    def createbodyjson(self, doc_type, typedict):
        properties = {}
        for k,v in typedict.items():
            properties[k] = self.createfield(v)
        body = {
            doc_type:{
               "properties" : properties
            }     
        }
        return json.dumps(body)

    def createfield(self, fieldtype):
        if(fieldtype == "smartcn"):
            return {"type": "text", "analyzer": "smartcn"}
        elif(fieldtype == "htmlsmartcn"):
            return {"type": "text", "analyzer": "htmlsmartcn"}
        elif(fieldtype == "no"):
            return {"type": "text", "index": "no"}
        elif(fieldtype == "not_analyzed"):
            return {"type": "text", "index": "not_analyzed"}
        elif(fieldtype == "date"):
            return {"type": "date"}
        elif(fieldtype == "int"):
            return {"type": "integer"}
        elif(fieldtype == "float"):
            return {"type": "float"}
        elif(fieldtype == "short"):
            return {"type": "short"}
        else:
            raise

if __name__ == "__main__" :
    #host = "10.104.142.196"
    host = "10.135.16.56"
    es = QuchuElastic(host, 9200)
    #es.test_requests()
    #es.analyzer("$$200")
    index = "testdb"
    es.deleteIndex(index)
    es.setall(index)

