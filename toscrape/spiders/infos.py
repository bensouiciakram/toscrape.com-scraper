import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import os 
from toscrape.items import ToscrapeItem
from scrapy.loader import ItemLoader
import re 
from scrapy.shell import inspect_response


class InfosSpider(CrawlSpider):
    name = 'infos'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://pstrial-2019-12-16.toscrape.com/browse/']
    


    rules = (
        Rule(LinkExtractor(allow='browse/'), callback='parse_item', follow=True),
    )

    keys = {
        'summertime':'Summertime',
        'insunsh':'In Sunsh',
        'rossignolnachtigall': 'Rossignol Nachtigall',
        'gatheringpotatoes': 'Gathering Potatoes',
        'courtprints': 'Court Prints',
        'owlman': 'Owl Man',
        'folfrom': 'Fol From',
        'shepherdswith': 'Shepherds With',
        'yukiprints': 'Yuki Prints',
        'aoshu': 'Ao Shu',
        'marcoricci': 'Marco Ricci',
        'tritonridden': 'Triton Ridden',
        'etcherprints': 'Etcher Prints',
        'gaitethe': 'Gaite The',
        'ilcollare': 'Il Collare',
        'searsbank': 'Sears Bank',
        'carnation': 'Carnation',
        'ubaldoembarking': 'Ubaldo Embarking',
        'belliedwoodpecker': 'Bellied Woodpecker',
        'barnowl': 'Barn Owl',
        'covercontemporary': 'Cover Contemporary',
        'wrapperfrom': 'Wrapper From',
        'straussphotography': 'Strauss Photography',
        'capitellilies': 'Capitel Lilies',
        'retreatsfor': 'Retreats For',
        'requiescatin': 'Requiescat In'
        }
    
    def parse_item(self, response):
        
        if ('insunsh' in response.url) or ( 'summertime' in response.url):
            browse_tree_string = response.url.replace(self.start_urls[0],'')
            print(browse_tree_string)

            total_products = int(response.xpath('//label/text()').re('\d+')[0])
            if (total_products/10).is_integer():
                total_pages = total_products//10
            else :
                total_pages = total_products//10 + 1
            categories = [self.keys[key] for key in browse_tree_string.split('/')]
            for  page_id in range(total_pages):
                yield Request(
                    response.url + '?page={}'.format(page_id),
                    callback = self.parse_page, 
                    meta = {
                    'browse_tree':categories,
                    }            
                )

    def parse_page(self,response):
         products_urls = [url for url in response.css('div#body').xpath('./div[2]/a/@href').getall() if not 'tarpit' in url ]
         base_url = 'http://pstrial-2019-12-16.toscrape.com'
         for product_url in products_urls :
             yield Request(
                 base_url + product_url,
                 callback = self.parse_product,
                 meta = {
                     'browse_tree':response.meta['browse_tree'],
                 }
             )

    def parse_product(self,response):
        loader = ItemLoader(ToscrapeItem(),response)
        loader.add_value('url',response.url)
        try:
            artist = ''.join(response.xpath('//h2[@class="artist"]/text()').get().split(':')[1]).split(',')[0]
            loader.add_value('artist',artist)
        except:
            pass
        loader.add_xpath('title','//h1/text()')
        loader.add_value('image','http://pstrial-2019-12-16.toscrape.com' + response.xpath('//div[@id="body"]/img/@src').get())
        loader.add_xpath('description','//div[@class="description"]/p/text()')
        try:
            dimentions = response.xpath('//table[@class="properties"]//td[contains(text(),"Dimensions")]/following-sibling::td/text()').re('\([\s\S]+?cm\)')[0]
            dim_image = dimentions.replace('(','').replace('cm','').replace(')','').split('x')
        except :
            pass
        try:            
            height = float(dim_image[0])
            loader.add_value('height',height)
        except :
            pass
        try:
            width = float(dim_image[1])
            loader.add_value('width',width)
        except: 
            pass
        
        # dim_sheet = dimentions[1]
        loader.add_value('categories',response.meta['browse_tree'])
        yield loader.load_item()
