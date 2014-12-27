import re
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
                #yield beer_item

    def parse_substyle(self, response):
        substyle = BeerStyleItem()
        for sel in response.xpath('//div[@class="inner"]/h2|//div[@class="inner"]/p|//div[@class="inner"]/table'):
            if sel:
                content = sel.extract()
                content = self.clean_text(content)
                if content:
                    if content[:4] == '<h2>':
                        print 'is a title'
                        print content
                        substyle['name'] = content
                    if content[:6] == '<p><b>':
                        print 'is a description'
                        print content
                        self.switch_desc(substyle, content)
                    if content[:6] == '<table':
                        print 'is a table'



    def clean_text(self, text):
        print "[DEBUG]: Clean text"

        if text:
            translation_table = dict.fromkeys(map(ord, '\t\r\n'), None)
            text = text.translate(translation_table)
            return text
        else:
            return None

    def clean_tags(self, text):
        print "[DEBUG]: Clean tags"

        if text:
            re.sub('<[^>]*>', '', text)
            return text
        else:
            return None

    def switch_desc(self,style,text):
        val = re.search( r"<b>.*?</b>", text, re.M|re.I).group()
        if val == '<b>Aroma:</b>':
            print 'Aroma descrip'
            ctext = self.clean_tags(text)
            style['aroma'] = ctext
        elif val == '<b>Appearance:</b>':
            print 'Appearance descrip'
            ctext = self.clean_tags(text)
            style['apper'] = ctext
        elif val == '<b>Flavor:</b>':
            print 'Flavor descrip'
            ctext = self.clean_tags(text)
            style['flavor'] = ctext
        elif val == '<b>Mouthfeel:</b>':
            print 'Mouthfeel descrip'
            ctext = self.clean_tags(text)
            style['mouthfeel'] = ctext
        elif val == '<b>Overall Impression:</b>':
            print 'Overall Impression descrip'
            ctext = self.clean_tags(text)
            style['overall'] = ctext
        elif val == '<b>Comments:</b>':
            print 'Comments descrip'
            ctext = self.clean_tags(text)
            style['comments'] = ctext
        elif val == '<b>History:</b>':
            print 'History descrip'
            ctext = self.clean_tags(text)
            style['history'] = ctext
        elif val == '<b>Ingredients:</b>':
            print 'Ingredients descrip'
            ctext = self.clean_tags(text)
            style['ingredients'] = ctext
        elif val == '<b>Commercial Examples:</b>':
            print 'Commercial Examples descrip'
            ctext = self.clean_tags(text)
            style['examples'] = ctext
        else:
            print 'Description not categorized'
        return None
