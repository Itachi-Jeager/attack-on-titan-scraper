import scrapy


class AotLocationsSpider(scrapy.Spider):

    # spider name
    name = "aot_locations"
    allowed_domains = ["attackontitan.fandom.com"]
    start_urls = ["https://attackontitan.fandom.com/wiki/Category:Locations_(Anime)"]

    def parse(self, response):
        """
        Function for looping through the location entries and retrieving links
        :params self
        :params response
        """
        for entry in response.css("div.category-page__members-wrapper"):
            location_link = entry.css("a.category-page__member-link").attrib["href"]

            request = scrapy.follow(location_link, callback=self.article_reader)

            request.meta["item"] = location_link

            yield request

    @staticmethod
    def article_reader(response):
        """
        The scraper which gets the data from individual pages
        :params response
        :return generator
        """
        # Section of the page containing data
        info_block = response.css(
            "div#mw-content-text "
            "aside.portable-infobox.pi-background.pi-border-color.pi-theme-wikia.pi-layout-default"
        )

        # territory data
        territory_div = info_block.xpath(".//div[@data-source='Territory']")
        territory = territory_div.css("div.pi-data-value.pi-font *::text").get()

        # notable inhabitants data
        notable_inhabitants_div = info_block.xpath(
            ".//div[@data-source='Notable inhabitants']"
        )
        notable_inhabitants = notable_inhabitants_div.css(
            "div.pi-data-value.pi-font *::text"
        ).getall()

        # notable former inhabitants data
        notable_former_inhabitants_div = info_block.xpath(
            ".//div[@data-source='Notable f. Inhabitants']"
        )
        if notable_former_inhabitants_div is not None:
            notable_former_inhabitants = notable_former_inhabitants_div.css(
                "div.pi-data-value.pi-font *::text"
            ).getall()
        else:
            notable_former_inhabitants = []

        # Instantiate Itemloader
        news_item_loader = ItemLoader(item=HealthnewsscraperItem(), response=info_block)

        # Populating source, name, rel_location, residents fields.
        news_item_loader.add_value("source", response.meta["item"])
        news_item_loader.add_css("name", "div.pi-data-value.pi-font::text")
        news_item_loader.add_value("rel_location", territory)
        news_item_loader.add_value(
            "residents", notable_inhabitants + notable_former_inhabitants
        )
