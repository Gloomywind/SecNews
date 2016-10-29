# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class SecnewsPipeline(object):
    def process_item(self, item, spider):
        with open("item.json","a") as m:
			if item['title'] and item['date']:
				item['title'] = item['title'][0].strip()
				item['link'] = item['link'][0].strip()
				item['date'] = item['date'][0].strip()
				item['desc'] = item['desc'][0].strip()
				line = json.dumps(dict(item),ensure_ascii=False)+"\n"
				line = unicode.encode(line,'utf-8')
				m.write(line)