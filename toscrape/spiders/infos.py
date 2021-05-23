import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class InfosSpider(CrawlSpider):
    name = 'infos'
    allowed_domains = ['http://pstrial-2019-12-16.toscrape.com/browse']
    start_urls = ['http://http://pstrial-2019-12-16.toscrape.com/browse/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
