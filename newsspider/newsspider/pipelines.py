# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis

class NewsspiderPipeline(object):
    def __init__(self):
        #conn = redis.Redis('localhost',port=6379,db=0)
    
    def process_item(self, item, spider):
        for key in item:
            print(key,item[key])
        return item
