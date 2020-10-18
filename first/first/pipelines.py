# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import pymongo
from pymongo import MongoClient
import sys


class FirstPipeline:
    client = None

    def open_spider(self, spider):
        # self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.client = MongoClient(host='localhost', port=27017)
        print(sys.path)
        print('spider start...')

    def process_item(self, item, spider):
        db = self.client.db.qiubai
        col = db.duanzi
        col.insert({
            'author': item['author'],
            'content': item['content']
        })
        return item

    def close_spider(self, spider):
        print('spider end...')
