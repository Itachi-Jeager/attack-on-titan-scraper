# import modules
import scrapy
from scrapy.loader import ItemLoader
from ..items import AotTitanItem


class AotTitansSpider(scrapy.Spider):
    """
    A spider for scraping data about titans from the Attack on Titan Fandom wiki

    The spider uses the basic spider template from scrapy, which visits the,
    start_urls and applies the parse method to the response it receives from,
    the urls.

    Attributes:
        name: name of the spider, string for identifying this spider
        allowed_domains: list containing the domains allowed for the spiders
        start_urls: list of the urls to begin scraping
        custom_settings: dictionary of settings for this specific spider
    """

    name = "aot_titans"
    allowed_domains = ["attackontitan.fandom.com"]
    start_urls = [
        "https://attackontitan.fandom.com/wiki/Colossal_Titan_(Anime)",
        "https://attackontitan.fandom.com/wiki/Armored_Titan_(Anime)",
        "https://attackontitan.fandom.com/wiki/Attack_Titan_(Anime)",
        "https://attackontitan.fandom.com/wiki/Female_Titan_(Anime)",
        "https://attackontitan.fandom.com/wiki/Beast_Titan_(Anime)",
        "https://attackontitan.fandom.com/wiki/Jaw_Titan_(Anime)",
        "https://attackontitan.fandom.com/wiki/Founding_Titan_(Anime)",
        "https://attackontitan.fandom.com/wiki/Cart_Titan_(Anime)",
        "https://attackontitan.fandom.com/wiki/War_Hammer_Titan_(Anime)",
    ]
    custom_settings = {
        "FEEDS": {"./aot_scraper/scrapes/titan_data.jl": {"format": "jsonlines"}},
    }

    def parse(self, response):
        """
        Function for scraping titan information from the start_urls,
        and supplying scraped data to the item loader

        Args:
            response: response from start_urls
        """

        # page section with information to scrape
        info_block = response.css(
            "div#mw-content-text aside.portable-infobox.pi-background.pi-border-color.pi-theme-wikia.pi-layout-default"
        )

        # specific HTML elements with content
        height_div = info_block.xpath(".//div[@data-source='Height']")
        powers_div = info_block.xpath(".//div[@data-source='Abilities']")
        current_shifter = info_block.xpath(".//div[@data-source='Current inheritor(s)']")
        former_shifter = info_block.xpath(".//div[@data-source='Former inheritor(s)']")

        # TODO: Some height data is missing
        # TODO: Some data in the power column is being lost because they are within tags

        # text retrieval from HTML
        height_data = height_div.css("div.pi-data-value.pi-font *::text").get()
        powers_data = powers_div.css("div.pi-data-value.pi-font *::text").getall()
        current_shifters_data = current_shifter.css("div.pi-data-value.pi-font a::text").getall()
        former_shifters_data = former_shifter.css("div.pi-data-value.pi-font a::text").getall()

        # instantiate item loader
        titan_item_loader = ItemLoader(item=AotTitanItem(), selector=info_block)

        # use item loader to populate fields
        titan_item_loader.add_css("name", "div.pi-data-value.pi-font::text")
        titan_item_loader.add_value("height", height_data)
        titan_item_loader.add_value("powers", powers_data)
        titan_item_loader.add_value("shifters", current_shifters_data + former_shifters_data)

        yield titan_item_loader.load_item()

        
        # yield {
        #     'name': info_block.css("div.pi-data-value.pi-font::text").get(),
        #     'height': height_div.css("div.pi-data-value.pi-font span::text").get(),
        #     'powers': powers_div.css("div.pi-data-value.pi-font::text").getall(),
        #     'shifters': current_shifter.css("div.pi-data-value.pi-font a::text").getall()
        #                 + former_shifter.css("div.pi-data-value.pi-font a::text").getall()

        # }
        
