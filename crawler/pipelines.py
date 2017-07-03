# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class MongoDBPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://"
            + settings["MONGODB_USERNAME"] + ":"
            + settings["MONGODB_PASSWORD"] + "@"
            + settings["MONGODB_SERVER"] + "/"
            + settings["MONGODB_DB"])

        self.db = self.client[settings["MONGODB_DB"]]
        self.collection = self.db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
            if data =='<html><body/></html>':
                raise DropItem("Missing data!")
        self.collection.update({'url': item['url']}, dict(item), upsert=True)
        log.msg("Article added to MongoDB database!",
                level=log.DEBUG, spider=spider)
        return item
