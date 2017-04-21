#!/usr/bin/env python
# coding: utf-8

"""
@file: iqiyi_login.py
@time: 2017/4/20 16:27
"""
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random

def main():
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    uaList = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Mozilla/5.0 (Windows;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
    ]
    dcap['phantomjs.page.settings.userAgent'] = (random.choice(uaList))
    driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--load-images=no'])
    #driver.get('http://m.iqiyi.com/v_19rrmmdbkg.html')
    driver.get('http://www.tianyancha.com/human/2065961364')
    #driver.get_screenshot_as_file('03.png')
    eles = driver.find_element_by_xpath('/html/body')
    html = eles.get_attribute('innerHTML')
    print "spider ", html
    driver.quit()

if __name__ == "__main__":
    main()
