# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import modules
import scrapy
from itemloaders.processors import Join, TakeFirst, MapCompose, Identity, Compose
from w3lib.html import remove_tags
import re
import unicodedata


def remove_cross(text: str) -> str:
    """
    Helper function which removes crosses and
    question marks from text.

    Args:
        text: scraped string.

    Returns:
        text: clean string
    """
    if "†" in text:
        text = text.replace("†", " ")
        return text
    if "?" in text:
        text = text.replace("?", " ")
        return text
    else:
        return text

 
def is_english(text):
    return text.isalpha() and unicodedata.name(text).startswith(('LATIN', 'COMMON'))
 
def remove_non_english(data):
    # output = []
    filtered = filter(is_english, data)
    english_str = ''.join(filtered)
    # output.append(english_str)
    return english_str


def remove_citations(text: str) -> str:
    """
    Helper function which removes citations from text.

    Args:
        text: scraped string

    Returns:
        clean_text: clean scraped string
    """

    # regex to substitute any square brackets with digits with an empty space
    clean_text = re.sub(r"\[\d\]", " ", text)
    return clean_text


def remove_trailing_spaces(text: str) -> str:
    """
    Helper function for removing trailing whitespaces

    Args:
        text: scraped string

    Returns:
        clean_text: clean scraped string
    """
    clean_text = text.strip()
    return clean_text


def remove_empty_entries(payload: list) -> list:
    """
    Helper function for removing empty or non-data entries from a list

    Args:
        payload: scraped list

    Returns:
        clean_payload: clean scraped list
    """
    # try:
    #     payload.remove(" ")

    # except ValueError as ve:
    #     return payload

    # filter out only list elements which aren't empty space or brackets
    clean_payload = list(filter(lambda entry: entry != " ", payload))
    clean_payload = list(filter(lambda entry: entry != ")", clean_payload))
    clean_payload = list(filter(lambda entry: entry != " )", clean_payload))
    clean_payload = list(filter(lambda entry: entry != "(", clean_payload))
    clean_payload = list(filter(lambda entry: entry != " (", clean_payload))
    return clean_payload


class AotLocationItem(scrapy.Item):
    """
    Item Loader for Attack on Titan Locations Scrape

    This class only contains attributes which are fields to be
    populated. The attributes use input and output processors to
    clean the data.

    Attributes:
        source: a URL, which is the source of the scraped data.
        name: a string, which is the name of the location
        rel_location: a string, which is the location related to current location scraped
        residents: a list of notable current and former residents of this location
    """

    # fields and their processors
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


class AotTitanItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_trailing_spaces), output_processor=TakeFirst()
    )
    height = scrapy.Field(
        input_processor=MapCompose(remove_trailing_spaces), output_processor=TakeFirst()
    )
    powers = scrapy.Field()
    shifters = scrapy.Field()

# put the correct filters for the Org Item class
class AotOrgItem(scrapy.Item):
    """An Item Loader for the Attack On Titan Organizations Scrape

    This class only contains attributes which are fields to be
    populated. The attributes use input and output processors to
    clean the data.

    Attributes:
        source: the source URL for the data
        name: the name of the organization
        role: the function of the organization
        leader: the leader of the organization
        former_members: the former members of the organization
        members: the members of the organization
        affiliation: the affiliations the organization has
    """
    source = scrapy.Field()
    name = scrapy.Field(
        input_processor=Identity(), output_processor=Compose(TakeFirst(), remove_trailing_spaces)
    )
    role = scrapy.Field()
    leader = scrapy.Field()
    members = scrapy.Field(input_processor=MapCompose(remove_cross), output_processor=Compose(remove_empty_entries))
    former_members = scrapy.Field(input_processor=MapCompose(remove_cross), output_processor=Compose(remove_empty_entries))
    affiliation = scrapy.Field(input_processor=Identity(), output_processor=remove_empty_entries)




# from dataclasses import dataclass, field
# from typing import Optional

# @dataclass
# class InventoryItem:
#     name: Optional[str] = field(default=None)
#     price: Optional[float] = field(default=None)
#     stock: Optional[int] = field(default=None)
