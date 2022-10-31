import scrapy

class amazon_crawler(scrapy.Spider):
    name = "products"
    start_urls = [
        "https://www.amazon.in/s?k=data science book"
    ]
    def parse(self, response, **kwargs):
        product_name = response.css(".a-color-base.a-text-normal::text").extract()
        yield {"product_name": product_name}