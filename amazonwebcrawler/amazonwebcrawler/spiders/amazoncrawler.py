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
        product_author = response.css(".a-color-secondary .a-size-base:nth-child(2)").css("::text").extract()
        product_price = response.css(".s-price-instructions-style .a-price-whole").css("::text").extract()
        product_reviews = response.css(".s-link-centralized-style .s-link-centralized-style , .widgetId\=search-results_3 .a-size-small").css("::text").extract()


        products["product_name"] = product_name
        products["product_author"] = product_author
        products["product_price"] = product_price
        products["product_reviews"] = product_reviews
        print("name ",len(product_name), "author ",len(product_author),"price ",len(product_price), "reviews ",len(product_reviews))
        yield products