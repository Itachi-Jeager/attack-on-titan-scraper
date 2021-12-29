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



        pass
 