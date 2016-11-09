# -*- coding: utf-8 -*-
__author__ =  "olenji"
'''
    date    :2016-10-24 16:20
    function:   数据库插入
    py_version  : 2.7
'''

import json,MySQLdb, sys,datetime
class JSONDataManager:

    conn = None
    cur = None
    def initConn(self):
        if self.conn :
            print "连接存在"
            return
        else:
            print "connect..."
            self.conn = MySQLdb.connect(host='56f214b4408fa.gz.cdb.myqcloud.com',user='cdb_outerroot',passwd='quchu2015',db='quchu',port=12020, charset='utf8')
            self.localconn = MySQLdb.connect(host='localhost',user='root',passwd='',db='wechatspider',port=3306,charset="utf8")
            print "create cursor..."
            self.cur = self.conn.cursor()
            self.localcur = self.localconn.cursor()

    def __del__(self):
        self.closeConn()

    def closeConn(self):
        if self.cur:
            print "close cursor..."
            self.cur.close()
        if self.localcur:
            print "close local cursor..."
            self.localcur.close()
        if self.conn:
            self.conn.commit()
            print "close connection..."
            self.conn.close()
        if self.localconn:
            self.localconn.commit()
            print "close local connection..."
            self.localconn.close()

    def exe(self):
        querysql = "select id,name from place"
        self.cur.execute(querysql)
        placelist = self.cur.fetchall()
        start_index = 100
        now = datetime.datetime.now()
        nextcraltime = now +  datetime.timedelta(minutes=5)
        
        for place in placelist:
            placename = place[1].replace('\'','\\\'')
            insertsql = "insert into wechat_word values(%s,2,'%s','%s',800,'%s', now() )" %(start_index,placename,place[0],nextcraltime )
            start_index+=1
            nextcraltime += datetime.timedelta(seconds=1)
            print insertsql
            self.localcur.execute(insertsql)
    '''
        self.cursor.execute(sql)
        self.cursor.fetchone()
        self.cursor.fetchall()
        self.cursor.fetchmany()
        self.cursor.lastrowid
        self.cursor.statement
        self.cursor.with_rows
        self.column_names
    '''
        

'''
    def readFile(self, filename):
        temp = open(filename, 'r')
        for line in temp:
            jsonline = json.loads(line)
            if jsonline["entityId"] not in ["NULL", "Null", "null"]:
                yield jsonline


    def insertViewRecord(self,userid,placeid):
        tablename = "view_action"
        querySql = "select * from " + tablename + " where user_id = " + userid + \
            " and place_id = " + placeid
        temp = self.cur.execute(querySql)
        if temp :
            updateSql = "update %s set times=times+1 where user_id = %s and place_id = %s" % (tablename, userid, placeid )
            self.cur.execute(updateSql)
        else:
            insertSql = "insert into " + tablename + " (user_id, place_id, create_tm, last_tm) values (%s, %s, %s, %s )" % (userid, placeid,time.time(), time.time())
            self.cur.execute(insertSql) 

    def olenji(self,filename):
        for row in self.readFile(filename):
            if row['event'] and row['event'] == "view":
                self.insertViewRecord(row['entityId'], row['targetEntityId'])
        

    def olenjidir(self, floder):
        for f in os.listdir(floder):
            if re.search('action',f):
                self.olenji(floder + '/' + f)
'''
            
        
    
if __name__ == '__main__':
    b = JSONDataManager()
    b.initConn()
  #  b.olenji()
    b.exe()