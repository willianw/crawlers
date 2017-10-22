# -*- coding: utf-8 -*-
import scrapy, json, pdb
from scrapy.selector import Selector

field_list=[
    u'name',
    u'index year',
    u'overall score',
    u'property rights',
    u'government integrity',
    u'judicial effectiveness',
    u'tax burden',
    u'government spending',
    u'fiscal health',
    u'business freedom',
    u'labor freedom',
    u'monetary freedom',
    u'trade freedom',
    u'investment freedom',
    u'financial freedom',
]

class EconomicFreedomSpider(scrapy.Spider):
    name = 'economic_freedom'
    allowed_domains = []
    start_urls = ['http://www.heritage.org/index/explore']
    custom_settings = {
        'FEED_FORMAT':'csv',
        'FEED_URI': 'output/economic_freedom.csv',
    }
    
    def parse(self, response):
        items = {}
        table = Selector(response).xpath("//table[@id='ctl00_cphContent_ExpMulti_GridView1']")
        fields = table.xpath("thead/tr/th/text()").extract()
        for i in range(1, len(fields)):
            field = fields[i]
            for item in table.xpath("tbody/tr"):
                name = item.xpath("td[1]/a/text()").extract_first()
                if not name in items:
                    items[name] = EconomicFreedomSpiderItem()
                    items[name]['name'] = name
                items[name][field] = item.xpath("td[%d]/span/text()" % (i + 1)).extract_first()
        for item in items.values():
            yield item
        

class EconomicFreedomSpiderItem(scrapy.Item):
	fields = {f:scrapy.Field() for f in field_list}
