#encoding:utf-8

'''
 author     : olenji
 date       : 2016-11-8 14:20:00
 function   : 封装了处理ElasticSearch的API
 py_version ：2.7.2
'''

from datetime import datetime
from elasticsearch import Elasticsearch
import requests, json

class ESProcess(object):

    es = doc_type = doc_index = None
    def __init__(self, h, p):
        self.baseurl = "http://%s:%d" % (h,p)
        self.es = Elasticsearch(host = h, port = p)
    
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

    #分析
    def analyzer(self, words):
        url =  self.baseurl + '/_analyze'
        params = {'analyzer': 'ik_max_word', 'pretty' : True , 'text' : words}
        req =  requests.get(url, params = params)
        print req.content
        return req
    
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


if __name__ == "__main__" :
    #host = "10.104.142.196"
    host = "10.135.16.56"
    es = ESProcess(host, 9200)
    es.setIndex("my-index")
    es.doc_type = "test-type"
    #es.test_requests()
    es.setIndex("nuomi_deal")
    es.doc_type = "deal"
    words = '欢唱KTV(莲花)'
    #es.analyzer(words)
    es.xiancheng_search("虎铁")
