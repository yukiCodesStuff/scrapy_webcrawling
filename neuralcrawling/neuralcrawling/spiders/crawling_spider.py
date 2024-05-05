from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider): # inherit from crawl spider class
    name = "myCrawler" # identifier for cl
    allowed_domains = [
        "toscrape.com"
    ]
    start_urls = ["http://books.toscrape.com/"]

    # crawl links that fit these rules (path variables)
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )

    def parse_item(self, response):
