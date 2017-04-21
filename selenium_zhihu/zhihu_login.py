#!/usr/bin/env python
# coding: utf-8

"""
@file: zhihu_login.py
@time: 2017/4/20 15:55
"""
from selenium import webdriver
import time

def main():
    brow = webdriver.Firefox()
    brow.set_page_load_timeout(20)
    brow.get('https://www.zhihu.com/#signin')
    ele = brow.find_element_by_name('account').send_keys('798990255@qq.com')
    ele = brow.find_element_by_name('password').send_keys('abcd1f2')

    brow.find_element_by_class_name('sign-button submit').click()
    time.sleep(7)
    brow.close()

if __name__ == "__main__":
    main()
