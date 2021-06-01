import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class KeysGeneratorSpider(CrawlSpider):
    name = 'keys_generator'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://pstrial-2019-12-16.toscrape.com/browse/summertime/']

    rules = (
        Rule(LinkExtractor(allow='browse/summertime/'), callback='parse_item', follow=True),
    )

    keys_values = set()

    def parse_item(self, response):
        self.keys_values.add((response.url.split('/')[-1],response.xpath('//h1[contains(text(),"Browse")]/text()').get().replace('Browse - ','')))
        print(self.keys_values)
