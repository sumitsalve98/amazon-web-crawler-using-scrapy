import scrapy
from ..items import AmazonwebcrawlerItem

class amazon_crawler(scrapy.Spider):
    name = "amazon_crawler"
    start_urls = [
        "https://www.amazon.in/s?k=data science book"
    ]
    def parse(self, response, **kwargs):
        products = AmazonwebcrawlerItem()
        product_name = response.css(".a-color-base.a-text-normal::text").extract()
        products["product_name"] = product_name
        yield products