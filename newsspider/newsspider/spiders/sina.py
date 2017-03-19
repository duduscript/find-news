# -*- coding: utf-8 -*-
import scrapy
from newsspider.items import NewsspiderItem


class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://sina.com.cn/']

    def __init__(self):
        self.urls = set(['http://sina.com.cn/'])

    def is_sina_news(self, url):
        return url not in self.urls

    def parse(self, response):
        links = response.xpath('//a[@href]/@href').extract()
        for link in links:
            if self.is_sina_news(link):
                self.urls.add(link)
                yield scrapy.Request(link,callback=self.parse_news)
    
    def parse_news(self, response):
        links = response.xpath('//a[@href]/@href').extract()
        for link in links:
            if self.is_sina_news(link):
                self.urls.add(link)
                yield scrapy.Request(link,callback=self.parse_news)
        
        item = NewsspiderItem()
        print(response.url)
        item['url'] = response.url
        item['title'] = response.xpath('//*[@id="main_title"]').extract()
        item['content'] = response.xpath('//*[@id="artibody"]').extract()
        if item['url'] != None and item['title'] != None and item['content'] != None:
            yield item
        