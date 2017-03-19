# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    def parse(self, response):
        item = ItemLoader(item=NewsspiderItem(),response=response)
        item.add_xpath('url',response.url)
        item.add_xpath('title','//*[@id="main_title"]')
        item.add_xpath('content','//*[@id="artibody"]')
        return l.load_item()
