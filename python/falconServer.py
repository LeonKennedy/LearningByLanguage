# -*- coding: utf-8 -*- 
# file: server.py 
# usage: cd into 'engine' folder and then run the server with the command below
#        gunicorn --bind 0.0.0.0:8000 --workers 2 --threads 2 --reload server

import falcon
import json
import numpy as np
import random

from entry_audit.entry_audit import EntryAudit
from freight_audit.freight_audit import FreightAudit

class EntryAuditService(object):
    def on_post(self, req, resp):
        '''
        Sample input
            [
                {"id": 1, "x": 0.1, "y": 0.1}, 
                {"id": 2, "x": 0.2, "y": 0.234},
                {"id": 3, "x": 0.3, "y": 0.3},
                {"id": 4, "x": 0.4, "y": 0.4},
                {"id": 5, "x": 0.5, "y": 0.5},
                {"id": 6, "x": 0.6, "y": 0.6},
                {"id": 7, "x": 0.7, "y": 0.7},
                {"id": 8, "x": 0.8, "y": 0.8},
                {"id": 9, "x": 0.9, "y": 0.9}
            ]

        Note: 
            1. id is mandatory in each record
            2. all the records shoud have the same fields

        Sample output (success): 
            {
                "msg": "",
                "data": [
                    {
                        "c": 0.97255282533357323,
                        "id": 2
                    }
                ],
                "success": true
            }        

        Sample output (fail):
            {
                "msg": "Invalid json input",
                "data": [],
                "success": false
            }
        '''
        # get/check input data
        data = req.bounded_stream.read()
        doc = None
        try:
            doc = json.loads(data)
            if len(doc) == 0:
                result = {'success': False, 'data': [], 'msg': 'Empty input'}
                resp.body = json.dumps(result)
                resp.status = falcon.HTTP_200
                return
        except:
            result = {'success': False, 'data': [], 'msg': 'Invalid json input'}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_200
            return

        # transform into numpy array
        table = [item.values() for item in doc]
        table = np.array(table)

        # build column indexes
        keys = doc[0].keys()
        id_index = None
        try: 
            id_index = keys.index('id')
        except:
            result = {'success': False, 'data': [], 'msg': 'Could not find mandatory field: id'}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_200
            return
        column_indexes = range(len(keys))
        column_indexes.remove(id_index) # exclude ids in regression

        # search outliers
        entry_audit = FreightAudit()
        outliers = None

        try: 
            outliers, confidences = entry_audit.get_outliers(table, column_indexes)
        except: 
            result = {'success': False, 'data': [], 'msg': 'Got exception while searching outliers'}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_200
            return

        # tidy results and return
        outlier_ids = table[outliers, id_index]

        data = [{'id': outlier_id, 'c': confidence}
                for outlier_id, confidence in zip(outlier_ids, confidences)]
        result = {'success': True, 'data': data, 'msg': ''}
        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200


class FreightAuditService(object):
    def on_post(self, req, resp):
        # get/check input data
        data = req.bounded_stream.read()
        doc = None
        try:
            doc = json.loads(data)
            if len(doc) == 0:
                result = {'success': False, 'data': [], 'msg': 'Empty input'}
                resp.body = json.dumps(result)
                resp.status = falcon.HTTP_200
                return
        except:
            result = {'success': False, 'data': [], 'msg': 'Invalid json input'}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_200
            return

        # transform into numpy array
        table = [item.values() for item in doc]
        table = np.array(table)

        # build column indexes
        keys = doc[0].keys()
        id_index = None
        try: 
            id_index = keys.index('id')
        except:
            result = {'success': False, 'data': [], 'msg': 'Could not find mandatory field: id'}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_200
            return
        column_indexes = range(len(keys))
        column_indexes.remove(id_index) # exclude ids in regression

        # search outliers
        freight_audit = FreightAudit()
        outliers = None

        try: 
            outliers, confidences = freight_audit.utliers_by_ransac(table, column_indexes)
        except: 
            result = {'success': False, 'data': [], 'msg': 'Got exception while searching outliers'}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_200
            return

        # tidy results and return
        outlier_ids = table[outliers, id_index]

        data = [{'id': outlier_id, 'c': confidence}
                for outlier_id, confidence in zip(outlier_ids, confidences)]
        result = {'success': True, 'data': data, 'msg': ''}
        resp.body = json.dumps(result)
        resp.status = falcon.HTTP_200


entry_audit_service = EntryAuditService()
freight_audit_service = FreightAuditService()
api = application = falcon.API()
api.add_route('/api/entry_audit', entry_audit_service)
api.add_route('/api/freight_audit', freight_audit_service)
