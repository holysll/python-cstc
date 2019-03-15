# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CstcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    url = scrapy.Field()  # 链接
    # source = scrapy.Field()  # 来源
    post_time = scrapy.Field()  # 发表时间
    content = scrapy.Field()  # 内容
