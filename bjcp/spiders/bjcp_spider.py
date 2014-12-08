from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from bjcp.items import BeerTitleItem, BeerStyleItem

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
        # filename = response.url.split("/")[-1] + ".html"
        # with open('.\\files\\'+filename, 'w') as f:
        #     f.write(response.body)
        for sel in response.xpath('//div[@class="inner"]/h2'):
            if sel:
                substyle = BeerStyleItem()
                print "error1"
                substyle['name'] = sel.extract()
                print "error2"
                yield substyle
