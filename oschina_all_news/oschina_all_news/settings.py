# -*- coding: utf-8 -*-

# Scrapy settings for oschina_all_news project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'oschina_all_news'

#爬虫目录
SPIDER_MODULES = ['oschina_all_news.spiders']
NEWSPIDER_MODULE = 'oschina_all_news.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'oschina_all_news (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发请求数
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#下载延迟 访问太快 限制访问  每3秒执行一次
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#每一个域名最多16个并发，一个域名含有多个IP的情况下
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#每一个IP最多16个并发，如果一个网站有多个IP时，那么并发就是域名并发*IP并发
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#是否爬取cookie，是否返回cookie
#COOKIES_ENABLED = False
#调试代码中log中每一请求都会有cookie
#COOKIE_DEBUG = True

# Disable Telnet Console (enabled by default)
#telnet 127.0.0.1 6023 监听6023端口，telnet上去之后可以暂停、查看状态等
#telnet上去之后的命令
#est()
#help() 可以在源码中查看
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

#爬虫启动、停止、异常时候调用
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'oschina_all_news.middlewares.OschinaAllNewsSpiderMiddleware': 543,
#}

# 请求需要被下载时候调用 可以设置useragent等
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'oschina_all_news.middlewares.MyCustomDownloaderMiddleware': 543,
#    'oschina_all_news.middlewares.ProxyMiddleware': 100,
#    'oschina_all_news.middlewares.RandomUserAgent': 1, #随机user agent
#}

# CnblogsSpider 中有一个IP代理设置

#扩展 钩子
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'oschina_all_news.pipelines.OschinaAllNewsItem': 300,
}

#智能请求 智能限速
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#第一个请求延迟多少秒
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#最大延迟多少秒
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#上下波动范围，就是在之前定义并发基础上进行波动
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

#缓存 下次请求时候使用
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#1：广度优先 0：深度优先  设置队列里面的优先级  只能是0或者1两个值
#DEPTH_PRIORITY = 0
#DEPTH_LIMIT = 4

#去重设置
#DUPEFILTER_CLASS = 'day96.deplication.RepeatFilter'
