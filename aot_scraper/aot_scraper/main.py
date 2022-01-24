
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import signals

from multiprocessing import Pool
# TODO: Format this file

# process = CrawlerProcess(get_project_settings())

# def spider_runner(spider, state):
#     """
    
#     A function that calls and executes spiders
#     """
    
#     process.crawl(spider, deltafetch_reset=state)
#     running_spider = process.create_crawler(spider)
#     running_spider.signals.connect(add_item, signal=signals.item_passed)
#     return spider



# def add_item(item):
#     items = []
#     return items.append(item)
# class CustomCrawler(object):

#     def crawl(self, spider):
#         crawled_items = []

#         def add_item(item):
#             crawled_items.append(item)

#         process = CrawlerProcess()

#         crawler = Crawler(spider)
#         crawler.signals.connect(add_item, signals.item_scraped)
#         process.crawl(crawler)

#         process.start()

#         return crawled_items


# class CustomCrawler(object):

#     def crawl(self, spider):
#         crawled_items = []

#         def add_item(item):
#             crawled_items.append(item)

#         process = CrawlerProcess(get_project_settings())

#         # crawler = Crawler(spider)
#         crawler = process.create_crawler(spider)
#         crawler.signals.connect(add_item, signals.item_scraped)
#         process.crawl(crawler)

#         process.start()

#         return crawled_items


# def add_item(item, crawled_item):
#     crawled_item.append(item)

    


# class CustomCrawler(object):

#     def crawl(self, spiders: list) -> list:
#         result_list = []
        

#         process = CrawlerProcess(get_project_settings())

#         # crawler = Crawler(spider)
#         crawler = process.create_crawler(spiders)
#         crawler.signals.connect(add_item, signals.item_scraped)
#         process.crawl(crawler)

#         process.start()

#         return results

def scrape(spiders) -> list:
    scrape.crawled_items = []

    process = CrawlerProcess(get_project_settings())
    crawler = process.create_crawler(spiders)
    crawler.signals.connect(add_item, signals.item_scraped)
    process.crawl(crawler)
    process.start()
    return scrape.crawled_items


def add_item(item):
    scrape.crawled_items.append(item)
    
if __name__ == '__main__':
    # running_scraper = CustomCrawler()
    # final_result = running_scraper.crawl("aot_titans")
    # print(f"This is the final result {final_result}")

    pool = Pool()
    args = [(["aot_titans"])]
    print(pool.starmap(scrape, args))
    