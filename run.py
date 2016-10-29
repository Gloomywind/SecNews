from scrapy.crawler import CrawlerProcess,CrawlerRunner
from scrapy.utils.project import get_project_settings
from secNews.spiders.secNewsSpider import secNewsSpider
import ConfigParser

config = ConfigParser.ConfigParser()
crawler = CrawlerProcess(get_project_settings())
with open('rule.cfg','r') as cfg:
    config.readfp(cfg)
    for sec in config.sections():
        dic = {}
        for node in config.options(sec):
            dic[node] = config.get(sec,node)
        #spider = newsSpider(**dic)
        print dic
        crawler.crawl('secNews',**dic)
crawler.start()
