# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WinescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WineItem(scrapy.Item):
    auctiondate = scrapy.Field()
    name = scrapy.Field()
    vintage = scrapy.Field()
    bottlesize_l = scrapy.Field()
    origin = scrapy.Field()
    description = scrapy.Field()
    state = scrapy.Field()
    packaging = scrapy.Field()
    price = scrapy.Field()
    minimum_price = scrapy.Field()
    maximum_price = scrapy.Field()
