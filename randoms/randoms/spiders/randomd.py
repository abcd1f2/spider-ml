# -*- coding: utf-8 -*-
import scrapy


class RandomdSpider(scrapy.Spider):
    name = "randomd"
    allowed_domains = ["jianshu.com"]
    start_urls = ['http://jianshu.com/']

    def parse(self, response):
        print(response.body)
        pass
