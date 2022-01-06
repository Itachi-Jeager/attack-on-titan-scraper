# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, TakeFirst, MapCompose


class AotLocationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source = scrapy.Field()
    name = scrapy.Field()
    rel_location = scrapy.Field()
    residents = scrapy.Field()

