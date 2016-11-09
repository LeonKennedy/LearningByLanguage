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

    #删除节点
    def deleteIndex(self, index):
        rep = self.es.indices.delete(index=index)
        print rep
        return rep['acknowledged']

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
        

    def matchall(self, index, doc_type):
        url = self.baseurl + "/%s/_search" % (index)
        body = {
            "query":{"match_all": {}}
        }
        req = requests.get(url, data=json.dumps(body))
        print req.content
        return req
    # 查看指定内容 
    def get(self,id):
        url = self.baseurl + "/%s/%s/%s" % (self.doc_index, self,doc_type, str(id))

        pass

    def test_requests(self):
        url = 'http://10.104.142.196:9201/_cat/indices?v'
        req = requests.get(url)
        print req.content
        print dir(req)

    # 需要进一步包装的接口
    def _uncoverMethod(self):
        self.es.indices.create(index= 'test-index', ignore=[400,404])
        
        

if __name__ == "__main__" :
    host = "10.104.142.196"
    port = 9201
    es = ESProcess(host, port)
    es.setIndex("my-index")
    es.doc_type = "test-type"
    es.catIndices()
    es.index({'name':'leon','age':15})
    es.catIndices()
    es.matchall("my-index","test-type")
