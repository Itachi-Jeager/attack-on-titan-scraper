
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import signals

from multiprocessing import Pool





def scrape(spiders) -> list:
    """Calls the spiders, specifically when used with asynchronous applications

    Args:
        spiders (list): a list of valid spider names

    Returns:
        list: a list of dictionaries
    """
    scrape.crawled_items = []

    process = CrawlerProcess(get_project_settings())
    crawler = process.create_crawler(spiders)
    crawler.signals.connect(add_item, signals.item_scraped)
    process.crawl(crawler)
    process.start()
    return scrape.crawled_items


def add_item(item):
    """Helper function to the scrape function

    Args:
        item (spider): spider object
    """
    scrape.crawled_items.append(item)


def runner(spiders: list, state) -> None:
    """
    A function that calls a named spider
    :param spiders:spider
    :param state:1 (On), 0 (Off) state for deltafetch reset
    """

    # Get the project settings from settings.py
    process = CrawlerProcess(get_project_settings())

    # loop through the spiders in list
    for spider in spiders:
        process.crawl(spider, deltafetch_reset=state)

    # Start crawling
    process.start()
    
if __name__ == '__main__':
    # running_scraper = CustomCrawler()
    # final_result = running_scraper.crawl("aot_titans")
    # print(f"This is the final result {final_result}")

    # executing with multiprocessing pool
    # pool = Pool()
    # args = [(["aot_titans"])]
    # print(pool.starmap(scrape, args))

    # executing normally
    runner(['aot_titans'], state=1)
    