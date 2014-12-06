# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class BeerStyleItem(scrapy.Item):
    # code = scrapy.Field()
    style = scrapy.Field()
    desc = scrapy.Field()
    # aroma = scrapy.Field()
    # apper = scrapy.Field()
    # flavor = scrapy.Field()
    # mouthfeel = scrapy.Field()
    # overall = scrapy.Field()
    # comments = scrapy.Field()
    # ingredients = scrapy.Field()
    # examples = scrapy.Field()