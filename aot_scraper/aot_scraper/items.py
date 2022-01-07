# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# imports
import scrapy
from itemloaders.processors import Join, TakeFirst, MapCompose
from w3lib.html import remove_tags

# TODO: Preprocess the fields based on the received data


class AotLocationItem(scrapy.Item):

    source = scrapy.Field()
    name = scrapy.Field()
    rel_location = scrapy.Field()
    residents = scrapy.Field()
