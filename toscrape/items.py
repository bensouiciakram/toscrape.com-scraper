# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    artiste = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    height = scrapy.Field()
    width = scrapy.Field()
    description = scrapy.Field()
    categories = scrapy.Field()
    browse_tree = scrapy.Field()
