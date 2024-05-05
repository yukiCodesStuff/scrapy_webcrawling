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
        yield { # generator
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".instock.availability::text")[1].get().replace("\n", "").replace(" ", "")
        }