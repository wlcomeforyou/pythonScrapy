import scrapy


class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu-spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
