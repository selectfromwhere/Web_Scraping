#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import scraping_info as s_inf

browser = webdriver.Chrome(s_inf.path_biz)
# browser = webdriver.Chrome(chromedriver.path_home)

browser.get(s_inf.url)
browser.find_element_by_name('_username').send_keys(s_inf.user_name)
browser.find_element_by_name('_password').send_keys(s_inf.password)
browser.find_element_by_id('log_in').click()