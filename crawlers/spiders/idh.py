# -*- coding: utf-8 -*-
import scrapy, json, pdb
from scrapy.exporters import CsvItemExporter
from scrapy import signals

field_list=['name', 'idh']

class IdhSpider(scrapy.Spider):
	name = 'idh'
	allowed_domains = []
	start_urls = ['http://hdr.undp.org/sites/all/themes/hdr_theme/js/bars.json']

	custom_settings = {
		'FEED_FORMAT': 'csv'
	}

	def parse(self, response):
		pdb.set_trace()
		_list = [x for x in json.loads(response.body) if x['indicator'] == "Human Development Index (HDI)" and x['year'] == "2015"]
		for country in _list:
			item =  IdhSpiderItem(name=country['country'], idh=country['value'])
			yield item
        

class IdhSpiderItem(scrapy.Item):
	fields = {f:scrapy.Field() for f in field_list}
