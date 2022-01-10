# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# imports
import scrapy
from itemloaders.processors import Join, TakeFirst, MapCompose, Identity, Compose
from w3lib.html import remove_tags
import re

#TODO: Remove brackets in residents fields

def remove_cross(text: str) -> str:
    """
    Helper function which removes crosses and
    question marks from text.

    :param text
    :return: text
    """
    if "†" in text:
        text = text.replace("†", " ")
        return text
    if "?" in text:
        text = text.replace("?", " ")
        return text
    else:
        return text


def remove_citations(text: str) -> str:
    """
    Helper function which removes citations from text.

    :param text
    :return: clean_text
    """
    clean_text = re.sub(r"\[\d\]", " ", text)
    return clean_text


def remove_trailing_spaces(text: str) -> str:
    """
    Helper function for removing trailing whitespaces

    :param text
    :return: clean_text
    """
    clean_text = text.strip()
    return clean_text


def remove_empty_entries(payload: list) -> list:
    """
    Helper function for removing empty or non-data entries from a list

    :param payload
    return: clean_payload
    """
    # try:
    #     payload.remove(" ")

    # except ValueError as ve:
    #     return payload

    clean_payload = list(filter(lambda entry: entry != " ", payload))
    return clean_payload


class AotLocationItem(scrapy.Item):

    source = scrapy.Field(input_processor=Identity(), output_processor=TakeFirst())
    name = scrapy.Field(
        input_processor=MapCompose(remove_trailing_spaces), output_processor=TakeFirst()
    )
    rel_location = scrapy.Field(
        input_processor=MapCompose(remove_trailing_spaces), output_processor=TakeFirst()
    )
    residents = scrapy.Field(
        input_processor=MapCompose(remove_citations, remove_cross),
        output_processor=Compose(remove_empty_entries),
    )
