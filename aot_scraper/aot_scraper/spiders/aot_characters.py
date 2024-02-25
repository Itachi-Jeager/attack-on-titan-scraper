import scrapy
from scrapy.loader import ItemLoader
from ..items import AotCharItem


class AotCharactersSpider(scrapy.Spider):
    name = 'aot_characters'
    allowed_domains = ['attackontitan.fandom.com']
    start_urls = ['https://attackontitan.fandom.com/wiki/List_of_characters/Anime']
    custom_settings = {
        "FEEDS": {"./aot_scraper/scrapes/character_data.jl": {"format": "jsonlines"}},
    }

    def parse(self, response):
        """
        Function for retrieving individual pages from start_urls

        Args:
            response: response object
        """
        # loop through the HTML element containing links to other pages
        page = response.css("div#content div#mw-content-text div.mw-parser-output div")

        # retrieve links
        character_container = page.css('div.characterbox-container')
        found_links = character_container.css("div a::attr(href)").getall()
       
        for entry in found_links:

            # follow the retrieve links and call article reader to process them
            request = response.follow(entry, callback=self.article_reader)
            # store the current link as a request meta item
            request.meta["item"] = entry

            yield request


    @staticmethod
    def article_reader(response):
        """
        The scraper which gets the data from individual pages

        Args:
            response: response object from individual pages

        Return:
            item_loader object
        """
        # Section of the page containing data
        data_box = response.css("div#mw-content-text div.mw-parser-output aside")
        sections = data_box.css("section")
        

        # get name
        name = data_box.css("div.pi-data-value.pi-font::text").get()

        # get species
        species = sections.css("div.pi-data-value.pi-font *::text").get()

        # gender data
        gender_data = sections.xpath(".//div[@data-source='Gender']")
        # get gender
        if gender_data is not None:
            gender = gender_data.css("div.pi-data-value.pi-font *::text").get()
        else:
            gender=''

        # residence data
        res = sections.xpath(".//div[@data-source='Residence']")
        # get residence
        if res is not None:
            residence = res.css("div.pi-data-value.pi-font *::text").get()
        else:
            residence = ''

        # status data
        stat = sections.xpath(".//div[@data-source='Status']")
        # get status
        if stat is not None:
            status = stat.css("div.pi-data-value.pi-font *::text").get()
        else:
            status = ''

        # function data
        duty = sections.xpath(".//div[@data-source='Occupation']")
        # get function
        if duty is not None:
            function = duty.css("div.pi-data-value.pi-font *::text").get()
        else:
            function = ''

        # rank data
        rank_data = sections.xpath(".//div[@data-source='Rank']")
        # get rank
        if rank_data is not None:
            rank = rank_data.css("div.pi-data-value.pi-font *::text").get()
        else:
            rank = ''

        # affiliation data
        affi_data = sections.xpath(".//div[@data-source='Affiliation']")
        # get affiliations
        if affi_data is not None:
            affi = affi_data.css("div.pi-data-value.pi-font *::text").getall()
        else:
            affi = []

        # titan kill count data
        titan_kill_data = sections.xpath(".//div[@data-source='Titan kills']")
        # get titan kills
        if titan_kill_data is not None:
            titan_kill = titan_kill_data.css("div *::text").getall()
        else:
            titan_kill = []

        # relatives data
        rel = sections.xpath(".//div[@data-source='Relatives']")
        # get relative names
        if rel is not None:
            relatives = rel.css("div *::text").getall()
        else:
            relatives = []

        # births data
        birth = sections.xpath(".//div[@data-source='Birthplace']")
        # get place of births
        if birth is not None:
            place_of_birth = birth.css("div.pi-data-value.pi-font *::text").get()
        else:
            place_of_birth = ''
        

        

        # Instantiate Itemloader
        location_item_loader = ItemLoader(item=AotCharItem(), selector=data_box)

        # Populating fields.
        location_item_loader.add_value(
            "source", "attackontitan.fandom.com" + response.meta["item"]
        )
        location_item_loader.add_value("name", name)
        location_item_loader.add_value("species", species)
        location_item_loader.add_value("gender", gender)
        location_item_loader.add_value("residence", residence)
        location_item_loader.add_value("status", status)
        location_item_loader.add_value("function", function)
        location_item_loader.add_value("rank", rank)
        location_item_loader.add_value("affiliation", affi)
        location_item_loader.add_value("titan_kills", titan_kill)
        location_item_loader.add_value("relatives", relatives)
        location_item_loader.add_value("birth_place", place_of_birth)

        # Return item loader object ready to exported
        yield location_item_loader.load_item()

        # yield {
        #     "source": "attackontitan.fandom.com" + response.meta["item"],
        #     # "name": info_block.css("div.pi-data-value.pi-font::text").get(),
        #     # "rel_location": territory,
        #     # "residents": notable_inhabitants + notable_former_inhabitants,
        # }
