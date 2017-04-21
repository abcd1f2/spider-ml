#!/usr/bin/env python
#coding=utf8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import scrapy
import urlparse
import requests
from items import OschinaAllNewsItem

class OschinaSpider(scrapy.spider):
    name='oschina_all_news'
    allowed_domains = ['oschina.net']
    base_url = 'http://www.oschina.net'
    start_urls = (
            'http://www.oschina.net/news/industry',
            )
    utl_template = 'http://www.oschina.net/action/ajax/get_more_news_list?newsType=&p={0}'

    def __init__(self):
        pass

    def parse(self, response):
        self.parse_details(response)

        for i in xrange(2, 100):
            new_url = self.utl_template.format(i)
            requests.post(new_url)
            scrapy.Request(new_url, callback=self.parse_details)

    def parse_details(self, response):
        for details in response.xpath('//div[@id="all-news"]/div/div[@class="main-info box-aw"]'):
            ite = OschinaAllNewsItem()
            infos = details.xpath('a/span/text()').extract()
            if len(infos) > 0:
                ite.title = infos[0]

            infos = details.xpath('div[@class="sc sc-text text-gradient wrap summary"]/text()').extract()
            if len(infos) > 0:
                ite.summary = infos[0]

            infos = details.xpath('div[@class="from"]')
            dinfos = infos.xpath('span/a/text()').extract()
            if len(dinfos) > 0:
                ite.author = dinfos[0]

            dinfos = infos.xpath('span/text()').extract()
            if len(dinfos) > 0:
                ite.publish = dinfos[0]

            dinfos = infos.xpath('a/span/text()').extract()
            if len(dinfos) > 0:
                ite.comments = dinfos[0]

