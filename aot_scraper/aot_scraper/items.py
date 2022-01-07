# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, TakeFirst, MapCompose
from w3lib.html import remove_tags

#TODO: Comment this file properly
#TODO: Remove input processor from source and confirm that it still works
#TODO: Preprocess the fields based on the received data


class AotLocationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source = scrapy.Field(input_processor=MapCompose(remove_tags),
                         output_processor=TakeFirst())
    name = scrapy.Field()
    rel_location = scrapy.Field()
    residents = scrapy.Field()

