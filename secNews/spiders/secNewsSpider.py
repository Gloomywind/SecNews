import scrapy
from secNews.items import SecnewsItem
class secNewsSpider(scrapy.Spider):
	name = "secNews"
	def __init__(self,**rule):
			# type: (object) -> object
			super(secNewsSpider, self).__init__(**rule)
			self.rule = rule
			self.allowed_domains = [rule['allowed_domains']]
			self.start_urls = [rule['start_url']]

	
	def parse(self, response):
		item = SecnewsItem()
		for sel in response.xpath(self.rule['root_node']):
			item['title'] = sel.xpath(self.rule['title']).extract()
			item['link'] = sel.xpath(self.rule['link']).extract()
			item['date'] = sel.xpath(self.rule['date']).extract()
			item['desc'] = sel.xpath(self.rule['desc']).extract()
			yield item