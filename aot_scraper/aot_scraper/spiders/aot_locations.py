import scrapy


class AotLocationsSpider(scrapy.Spider):
    name = 'aot_locations'
    allowed_domains = ['attackontitan.fandom.com']
    start_urls = ['http://attackontitan.fandom.com/']

    def parse(self, response):
        pass
 