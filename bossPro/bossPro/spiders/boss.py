import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.boss.com']
    start_urls = ['http://www.boss.com/']

    def parse(self, response):
        pass
