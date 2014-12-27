# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst


class BeerTitleItem(scrapy.Item):
    code = Field(output_processor=TakeFirst())
    name = Field(output_processor=TakeFirst())
    url = Field(output_processor=TakeFirst())


class BeerStyleItem(scrapy.Item):
    code = Field(output_processor=TakeFirst())
    name = Field(output_processor=TakeFirst())
    desc = Field(output_processor=TakeFirst())
    aroma = Field(output_processor=TakeFirst())
    apper = Field(output_processor=TakeFirst())
    flavor = Field(output_processor=TakeFirst())
    mouthfeel = Field(output_processor=TakeFirst())
    overall = Field(output_processor=TakeFirst())
    comments = Field(output_processor=TakeFirst())
    history = Field(output_processor=TakeFirst())
    ingredients = Field(output_processor=TakeFirst())
    examples = Field(output_processor=TakeFirst())

