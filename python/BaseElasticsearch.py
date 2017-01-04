#encoding:utf-8

'''
 author     : olenji
 date       : 2016-11-30 16:00:00
 function   : 1.操作elasticsearch的基础类
 py_version ：2.7.2
'''

from datetime import datetime
from elasticsearch import Elasticsearch
import requests, json

class BaseElasticsearch(object):
    es_auth = ('elastic', 'quchu2015')

    es = doc_type = doc_index = None
    def __init__(self, h, p):
        self.baseurl = "http://%s:%d" % (h,p)
        self.es = Elasticsearch(host = h, port = p, http_auth=('elastic','quchu2015'))
        self.bf = BodyFactory()
    
    def setIndex(self,index):
        self.doc_index = index


    #=============创 建==============
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
            rep = requests.post(url, auth=es_auth, data=json.dumps(body))
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
        rep = requests.post(url, auth=es_auth, data=json.dumps(body))
        print(rep.content)
        return rep

    #创建Index的别名alias
    def createAlias(self, index, alias):
        url = self.baseurl + "/_aliases"
        body = {
            "actions":[
                { "add" : { "index" : index, "alias" : alias } } 
            ]
        }
        rep = requests.post(url, data = json.dumps(body))
        print rep.content
        return rep

    def deleteAlias(self, index, alias):
        url = self.baseurl + "/_aliases"
        body = {
            "actions":[
                { "remove" : { "index" : index, "alias" : alias } } 
            ]
        }
        rep = requests.post(url, data = json.dumps(body))
        print rep.content
        return rep


   #-----------------删除-----------
    #删除节点
    def deleteIndex(self, index):
        rep = self.es.indices.delete(index=index)
        print rep
        return rep['acknowledged']

   #删除 type
    def deleteType(self, index, doc_type):
        url = self.baseurl + "/%s/%s/_delete_by_query?pretty" % (index, doc_type)
        body = {
            "query":{"match_all": {}}
        }
        req = requests.post(url, data=json.dumps(body))
        print req.content
        return req


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

    # 查看结构mapping
    def mapping(self, index, doc_type):
        if doc_type:
            url = self.baseurl + "/%s/_mapping/%s?pretty" % (index, doc_type)
        else:
            url = self.baseurl + "/%s/_mapping?pretty" % (index)
        req = requests.get(url)
        print req.content
        return req
        
        

    def matchall(self, index, doc_type = None):
        if doc_type:
            url = self.baseurl + "/%s/%s/_search?pretty" % (index, doc_type)
        else:
            url = self.baseurl + "/%s/_search?pretty" % (index)
        body = {
            "query":{"match_all": {}},
            "size" : 1
        }
        req = requests.get(url, data=json.dumps(body))
        print req.content
        return req

    # 查看指定内容 
    def get(self,id):
        url = self.baseurl + "/%s/%s/%s" % (self.doc_index, self.doc_type, str(id))

    #根据关键字搜索
#   it is not good
    def search_by_key(self, keys):
        url = self.baseurl + "/%s/%s/_search?pretty" % (self.doc_index, self.doc_type)
        body = {
            'query': {
                'match':  keys
            }
        }
        req = requests.get(url, data = json.dumps(body))
        #print req.content
        return req

    def search_all(self, key, index, doc_type=None):
        if doc_type:
            url = self.baseurl + "/%s/%s" % (index, doc_type)
        else:
            url = self.baseurl + "/%s" % index
        body = {
            "query" : {
                "match" : key
            }     
        }
        return self.base_search(url, body)

    def base_search(self, url, body ):
        url = url +  "/_search?pretty" 
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
    
class BodyFactory(object):

    def createbody(self, doc_type, typedict):
        properties = {}
        for k,v in typedict.items():
            properties[k] = self.createfield(v)
        body = {
            doc_type:{
               "properties" : properties
            }     
        }
        return body

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
        elif(fieldtype == "double"):
            return {"type": "double"}
        elif(fieldtype == "short"):
            return {"type": "short"}
        elif(fieldtype == "point"):
            return {"type": "geo_point"}
        elif(fieldtype == "object"):
            return {"type": "object"}
        elif(fieldtype == "nested"):
            return {"type": "nested"}
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



