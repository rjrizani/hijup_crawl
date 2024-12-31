# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HijupItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    price_RP = scrapy.Field()
    description = scrapy.Field()
    material = scrapy.Field()
    size = scrapy.Field()
    color = scrapy.Field()

    url = scrapy.Field()
    img_url = scrapy.Field()
    availability = scrapy.Field()
    scraped_at = scrapy.Field()



#test


    
