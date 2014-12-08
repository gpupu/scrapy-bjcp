from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from bjcp.items import BeerTitleItem

__author__ = 'Gabriel'

class BJCPSpider(CrawlSpider):
    name = "bjcp"
    allowed_domains = ["bjcp.org"]
    start_urls = [
        "http://www.bjcp.org/2008styles/catdex.php"
    ]
    rules = (
        Rule(SgmlLinkExtractor("style\d\d.php"), callback='parse_substyle', follow=False),
    )

    def parse_start_url(self, response):
        for sel in response.xpath("//ul[@class='features']/li"):
            beer_item = BeerTitleItem()
            n = sel.xpath('a[@href]/text()').extract()
            if n:
                beer_item['name'] = n[0]
                beer_item['url'] = sel.xpath('a/@href').extract()[0]
                yield beer_item

    def parse_substyle(self, response):
        resp = HtmlXPathSelector(response)
        print "Respuesta del subestilo: "
        yield resp
        pass
        #titles = hxs.select('//span[@class="pl"]')
        items = []
        # for titles in titles:
        #     item = CraigslistSampleItem()
        #     item ["title"] = titles.select("a/text()").extract()
        #     item ["link"] = titles.select("a/@href").extract()
        #     items.append(item)

