# -*- coding: utf-8 -*-
import scrapy, json, pdb
from scrapy.selector import Selector

field_list=['name', 'efi']

class EconomicFreedomSpider(scrapy.Spider):
    name = 'economic_freedom'
    allowed_domains = []
    start_urls = ['http://www.heritage.org/index/explore']

    def parse(self, response):
	hxs = Selector(response)
	pdb.set_trace()
	for country in hxs.xpath("//table[@id='ctl00_cphContent_ExpMulti_GridView1']/tbody/tr"):
		item =  EconomicFreedomSpiderItem()
		item['name'] = country.xpath("td[@class='explore-country']/a/text()").extract_first()
		item['efi'] = country.xpath("td/span[contains(@id, 'lblYearScore')]/text()").extract_first()
		
		yield item
        

class EconomicFreedomSpiderItem(scrapy.Item):
	fields = {f:scrapy.Field() for f in field_list}
