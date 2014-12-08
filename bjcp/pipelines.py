# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class CleaningTextPipeline(object):
    def process_item(self, item, spider):
        print "[DEBUG]: Pipeline CleaningText"

        if item['name']:
            translation_table = dict.fromkeys(map(ord, '\t\r\n'), None)
            item['name'] = item['name'].translate(translation_table)
            return item
        else:
            raise DropItem("Item vacío %s" % item)


class RetrieveCodePipeline(object):
    def process_item(self,item, spider):
        print "[DEBUG]: Pipeline RetrieveCode"
        list = item['name'].split(".", 1)
        if len(list) > 1:
            item['code'] = list[0]
            item['name'] = list[1].strip()
            return item
        else:
            raise DropItem("Non code Item %s" % item)







