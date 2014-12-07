from bjcp.items import BeerTitleItem

__author__ = 'Gabriel'

import scrapy


# class DmozSpider(scrapy.Spider):
#     name = "dmoz"
#     allowed_domains = ["dmoz.org"]
#     start_urls = [
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#     ]
#
#     def parse(self, response):
#         for sel in response.xpath('//ul/li'):
#             item = DmozItem()
#             item['title'] = sel.xpath('a/text()').extract()
#             item['link'] = sel.xpath('a/@href').extract()
#             item['desc'] = sel.xpath('text()').extract()
#             yield item


class BJCPSpider(scrapy.Spider):
    name = "bjcp"
    allowed_domains = ["bjcp.org"]
    start_urls = [
        "http://www.bjcp.org/2008styles/catdex.php"
    ]

    def parse(self, response):
        for sel in response.xpath("//ul[@class='features']/li"):
            beer_item = BeerTitleItem()
            n = sel.xpath('a[@href]/text()').extract()
            if n:
                beer_item['name'] = n[0]
                beer_item['url'] = sel.xpath('a/@href').extract()[0]
                yield beer_item

