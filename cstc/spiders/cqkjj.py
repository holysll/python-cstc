# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from cstc.items import *
from cstc.loaders import *
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose
from w3lib.html import  remove_tags

class CqkjjSpider(CrawlSpider):
    name = 'cqkjj'
    allowed_domains = ['www.cstc.gov.cn']
    start_urls = ['http://www.cstc.gov.cn/']


    rules = (
        Rule(LinkExtractor(allow='http\:\/\/www\.cstc\.gov\.cn\/View\.aspx\?id\=\d', restrict_xpaths='//span[@id="tzList"]//table[@width="98%"]'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = CstcItem()
        item['title'] = str(response.xpath('//td[@class="14b2"]/text()').extract_first())
        item['url'] = str(response.url)
        item['content'] = ''.join(response.xpath( '//span[@class="titlefront"]//div/text()').extract()).replace("\\u3000","").replace("\t","").replace("\n","").replace("\r","")
        item['post_time'] = str(response.xpath( '//td[@class="date"]/text()').re_first('(\d+-\d+-\d+)'))
        #item['source'] = str(response.xpath('//td[@class="date"]/text()').re_first('来自： (.*)')) # .strip()
        yield item

        # loader = CqkjjLoader(item=CstcItem(), response=response)
        # loader.add_xpath('title', '//td[@class="14b2"]/text()',MapCompose())
        # loader.add_value('url', response.url)
        # loader.add_xpath('content', '//span[@class="titlefront"]//div/text()')
        # loader.add_xpath('post_time', '//td[@class="date"]/text()', re='(\d+-\d+-\d+)')
        # # loader.add_xpath('source', '//td[@class="date"]/text()', re='来自： (.*)')
        # yield loader.load_item()

