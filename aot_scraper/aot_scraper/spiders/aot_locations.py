import scrapy


class AotLocationsSpider(scrapy.Spider):
    name = 'aot_locations'
    allowed_domains = ['attackontitan.fandom.com']
    start_urls = ['https://attackontitan.fandom.com/wiki/Category:Locations_(Anime)']

    def parse(self, response):
        """
        Function for looping through the location entries and retrieving links
        :params self
        :params response
        """
        for entry in response.css("div.category-page__members-wrapper"):
            location_link = entry.css("a.category-page__member-link").attrib["href"]


            request = scrapy.follow(location_link, callback=self.article_reader)

            request.meta['item'] = location_link

            yield request


    @staticmethod
    def article_reader(response):
        """
        The scraper which gets the data from individual pages
        :params response
        :return generator
        """
        # Instantiating an item loader with an item and a response.
        info_block = response.css("div#mw-content-text")
        news_item_loader = ItemLoader(item=HealthnewsscraperItem(), response=info_block)
        
        # Populating the link, headline, body and date fields.
        news_item_loader.add_value('link', response.meta['item'])
        news_item_loader.add_css('name', 'aside.portable-infobox.pi-background.pi-border-color.pi-theme-wikia.pi-layout-default div.pi-data-value.pi-font::text')
        news_item_loader.add_css('description', 'p::text')
        news_item_loader.add_css('date_published', 'span.meta-date::text')


        pass
 