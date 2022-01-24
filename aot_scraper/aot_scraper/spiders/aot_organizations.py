import scrapy
from scrapy.loader import ItemLoader
from ..items import AotOrgItem


class AotOrganizationsSpider(scrapy.Spider):
    name = 'aot_organizations'
    allowed_domains = ['attackontitan.fandom.com']
    start_urls = ['https://attackontitan.fandom.com/wiki/Category:Organizations_(Anime)']
    custom_settings = {
        "FEEDS": {"./aot_scraper/scrapes/organization_data.jl": {"format": "jsonlines"}},
    }

    def parse(self, response):
        """
        Function for retrieving individual pages from start_urls

        Args:
            response: response object
        """
        # loop through the HTML element containing links to other pages
        for entry in response.css("div.category-page__members-wrapper"):
            # retrieve links
            organization_link = entry.css("a.category-page__member-link").attrib["href"]
            # follow the retrieve links and call article reader to process them
            request = response.follow(organization_link, callback=self.article_reader)
            # store the current link as a request meta item
            request.meta["item"] = organization_link

            yield request


# TODO: Check the webpage to determine the location of data
# TODO: Get Occupation data
# TODO: Add missing fields to yield data

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
        info_block = response.css(
            "div#mw-content-text aside.portable-infobox.pi-background.pi-border-color.pi-theme-wikia.pi-layout-default"
        )

        # leader data
        leader_div = info_block.xpath(".//div[@data-source='Leader']")
        leader = leader_div.css("div.pi-data-value.pi-font *::text").get()

        # members data
        members_div = info_block.xpath(
            ".//div[@data-source='Members']"
        )

        # check if members data exists
        if members_div is not None:
            members = members_div.css(
            "div.pi-data-value.pi-font *::text"
        ).getall() 
        else:
            members = []

        # notable members data
        notable_members_div = info_block.xpath(
            ".//div[@data-source='Notable members']"
        )

        # check if members data exists
        if notable_members_div is not None:
            notable_members = notable_members_div.css(
            "div.pi-data-value.pi-font *::text"
        ).getall() 
        else:
            notable_members = []
        

        # notable former members data
        notable_former_members_div = info_block.xpath(
            ".//div[@data-source='Notable f. Members']"
        )
        # check if former inhabitants data exists
        if notable_former_members_div is not None:
            notable_former_members = notable_former_members_div.css(
                "div.pi-data-value.pi-font *::text"
            ).getall()
        else:
            notable_former_members = []

        # Instantiate Itemloader
        location_item_loader = ItemLoader(item=AotOrgItem(), selector=info_block)

        # Populating source, name, rel_location, residents fields.
        location_item_loader.add_value(
            "source", "attackontitan.fandom.com" + response.meta["item"]
        )
        location_item_loader.add_css("name", "div.pi-data-value.pi-font::text")
        location_item_loader.add_value("leader", leader)
        location_item_loader.add_value(
            "residents", members + notable_members + notable_former_members
        )

        # Return item loader object ready to exported
        yield location_item_loader.load_item()

        # yield {
        #     "source": "attackontitan.fandom.com" + response.meta["item"],
        #     "name": info_block.css("div.pi-data-value.pi-font::text").get(),
        #     "rel_location": territory,
        #     "residents": notable_inhabitants + notable_former_inhabitants,
        # }
