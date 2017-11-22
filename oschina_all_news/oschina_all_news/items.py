# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import requests

from random import choice, sample, shuffle

class OschinaAllNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    summary = scrapy.Field()
    author = scrapy.Field()
    publish = scrapy.Field()
    comments = scrapy.Field()
