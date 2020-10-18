import scrapy

from first.items import FirstItem


class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu-spider'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        qiushi = response.xpath("//div[@id='content']//div[contains(@class, 'article')]")
        for qs in qiushi:
            author = qs.xpath("./div[contains(@class, 'author')]//h2/text()").extract()
            content = ''.join(qs.xpath("./a[contains(@class, 'contentHerf')]/div/span//text()").extract())
            item = FirstItem()
            item['author'] = author
            item['content'] = content
            yield item

