# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DroomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    model = scrapy.Field()
    price = scrapy.Field()
    fuel = scrapy.Field()
    location = scrapy.Field()
    km_drove = scrapy.Field()
    owner = scrapy.Field()
    url = scrapy.Field()