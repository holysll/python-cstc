# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CstcPipeline(object):
    def __init__(self):
         self.file = open("cstc_tzgg.csv", "w")
         self.file.write('post_time,title,url,content\n') # source,
    def process_item(self, item, spider):
        info = dict(item)
        self.file.write(info["post_time"]+","+info["title"]+","+info["url"]+","+info["content"].replace("\\u3000","").replace("\t","").replace("\n","").replace("\r","").strip()+"\n")
        return item #+info["source"].replace("\n","，").replace("\r",'')+","

    def close_spider(self, spider):
        self.file.close()