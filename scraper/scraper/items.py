# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class CategoryItem(scrapy.Item):
    name = scrapy.Field()
class LawyerItem(scrapy.Item):
    name = scrapy.Field()
    photo = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    office_location = scrapy.Field()
    website = scrapy.Field()
    categories = scrapy.Field()
    description = scrapy.Field()
    working_hours=  scrapy.Field()
    rating = scrapy.Field()