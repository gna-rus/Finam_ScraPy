import scrapy


class GazpSpider(scrapy.Spider):
    name = "GAZP"
    allowed_domains = ["www.finam.ru"]
    start_urls = ["http://www.finam.ru/"]

    def parse(self, response):
        pass
