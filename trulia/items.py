# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import scrapy

class TruliaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    retail_price = Field()
    bedrooms = Field()
    barthrooms = Field()
    area = Field()
    street_address = Field()
    region = Field()
    postal_code = Field()
    latitude = Field()
    longitude = Field()
