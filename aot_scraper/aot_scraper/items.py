# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# imports
import scrapy
from itemloaders.processors import Join, TakeFirst, MapCompose, Identity
from w3lib.html import remove_tags
import re

# TODO: source should be a string not list
# TODO: name should be a string not list
# TODO: related location should be a string not list
# TODO: residents sometimes has cross emoji
# TODO: remove the citations from residents
# TODO: remove invisible characters

def remove_cross(text: str) -> str:
    """
    Helper function which removes crosses and
    question marks from text.

    :param text
    :return: text
    """
    if "†" in text:
        text = text.replace("†", "")
        return text
    if "?" in text:
        text = text.replace("?", "")
        return text
    else:
        return text


def remove_citations(text: str) -> str:
    """
    Helper function which removes citations from text.

    :param text
    :return: text
    """
    clean_text = re.sub(r'\[\d\]', "", text)
    return clean_text



class AotLocationItem(scrapy.Item):

    source = scrapy.Field(input_processor=Identity(), output_processor=TakeFirst())
    name = scrapy.Field(input_processor=Identity(), output_processor=TakeFirst())
    rel_location = scrapy.Field(input_processor=Identity(), output_processor=TakeFirst())
    residents = scrapy.Field(input_processor=MapCompose(remove_citations, remove_cross), output_processor=Identity())
