#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import csv
import driver_path as chromedriver
import agent_site_url as site_url

browser = webdriver.Chrome(chromedriver.path)
browser.get(site_url.url)
browser.implicitly_wait(5)

f = open('csv/Agent_Detail_URL.csv','w')
writer = csv.writer(f, lineterminator='\n')
csvrecord = []

agentlists = browser.find_elements_by_class_name('company-box')
for agentlist in agentlists:
    agnturl = agentlist.find_elements_by_tag_name('a')
    for i in range(len(agnturl)):
        csvrecord.append(agnturl[i].get_attribute('href'))
        writer.writerow(csvrecord)
        csvrecord = []

browser.quit()
