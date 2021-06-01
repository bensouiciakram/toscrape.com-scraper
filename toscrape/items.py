# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class ToscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    artist = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    height = scrapy.Field(
        output_processor=TakeFirst()
    )
    width = scrapy.Field(
        output_processor=TakeFirst()
    )
    description = scrapy.Field()
    categories = scrapy.Field()
