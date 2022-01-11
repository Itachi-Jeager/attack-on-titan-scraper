import scrapy


class AotTitansSpider(scrapy.Spider):
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
        Function for scraping titan information
        :param response
        """
        info_block = response.css(
            "div#mw-content-text aside.portable-infobox.pi-background.pi-border-color.pi-theme-wikia.pi-layout-default"
        )
        height_div = info_block.xpath(".//div[@data-source='Height']")
        powers_div = info_block.xpath(".//div[@data-source='Abilities']")
        current_shifter = info_block.xpath(".//div[@data-source='Current inheritor(s)']")
        former_shifter = info_block.xpath(".//div[@data-source='Former inheritor(s)']")

        # TODO: Some height data is missing
        # TODO: Some data in the power column is being lost because they are within tags


        yield {
            'name': info_block.css("div.pi-data-value.pi-font::text").get(),
            'height': height_div.css("div.pi-data-value.pi-font span::text").get(),
            'powers': powers_div.css("div.pi-data-value.pi-font::text").getall(),
            'shifters': current_shifter.css("div.pi-data-value.pi-font a::text").getall()
                        + former_shifter.css("div.pi-data-value.pi-font a::text").getall()

        }
        
        
