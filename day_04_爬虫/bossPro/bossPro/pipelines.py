# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from redis import Redis
class BossproPipeline(object):
    fp = None
    def open_spider(self, spider):
        print('开始爬虫......')
        self.fp = open('./boss.txt','w',encoding='utf-8')
    def close_spider(self, spider):
        print('结束爬虫......')
        self.fp.close()
    #爬虫文件每向管道提交一次item,则该方法就会被调用一次.
    #参数:item 就是管道接收到的item类型对象

    def process_item(self, item, spider):
        #print(item)
        self.fp.write(item['job_name']+':'+item['salary']+':'+item['company']+'\n')
        return item #返回给下一个即将被执行的管道类

class mysqlPileLine(object):
    conn = None
    cursor =None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='',db='scrapy',charset="utf8")
        print(self.conn)
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        # print(item)
        #print('insert into boss values ("%s","%s","%s")'%(item['job_name'],item['salary'],item['company']))
        try:
            print('insert into boss values ("%s","%s","%s")'%(item['job_name'],item['salary'],item['company']))
            self.cursor.execute('insert into boss values ("%s","%s","%s")'%(item['job_name'],item['salary'],item['company']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
    def close_spider(self,spider):
        self.conn.close()
        self.cursor.close()

class redisPileLine(object):
    conn = None
    def open_spider(self,spider):
        self.conn = Redis(host='127.0.0.1',port=6379)
        print(self.conn)
    def process_item(self, item, spider):
        # print(item)
        dic = {
            'name':item['job_name'],
            'salary':item['salary'],
            'company':item['company']
        }
        self.conn.lpush('boss',dic)
