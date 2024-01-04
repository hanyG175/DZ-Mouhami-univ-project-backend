import scrapy
from scraper.items import CategoryItem


class BlackwidowSpider(scrapy.Spider):
    name = "BlackWidow"
    allowed_domains = ["avocatalgerien.com"]
    start_urls = ["https://avocatalgerien.com/categories/"]

    def parse(self, response):
        names = response.css('li.maincat a::text').getall()
        for name in names:
            yield CategoryItem(name=name)

