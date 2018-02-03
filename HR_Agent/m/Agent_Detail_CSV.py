#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import csv
import random
import driver_path as chromedriver

def getAgentDetail(csvrecord):
    dic = {}

    # 社名
    corp = browser.find_element_by_xpath('//*[@id="content-article"]/div[1]/div[1]/div/div/div/div[1]/div/p[2]').text
    dic.setdefault('社名',corp)

    # table-dから、['注力職種']['注力エリア']を取得
    # table-eから、['本社所在地']['設立']['転職エージェント数']['職業紹介許可番号']['紹介事業許可年']を取得
    table = ['table-d','table-e']
    for n in range(len(table)):
        items = browser.find_element_by_class_name(table[n]).find_elements_by_tag_name('dl')
        for i in range(len(items)):
            dic.setdefault(items[i].find_element_by_tag_name('dt').text,items[i].find_element_by_tag_name('dd').text)
    # ホームページ
    try:
        url = browser.find_element_by_class_name('table-e').find_element_by_tag_name('a').get_attribute('href')
        dic.setdefault('ホームページ',url)
    except:
        pass

    for i in range(len(header)):
        if header[i] in dic:
            csvrecord.append(dic[header[i]].replace("\n"," "))
        else:
            csvrecord.append('登録なし')



options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
options.add_argument('--blink-settings=imagesEnabled=false')
browser = webdriver.Chrome(chromedriver.path,chrome_options=options)

f = open('Agent_Detail.csv','w')
writer = csv.writer(f, lineterminator='\n')
header = ['社名','本社所在地','設立','転職エージェント数','職業紹介許可番号','紹介事業許可年','ホームページ','注力職種','注力エリア']
writer.writerow(header)

with open('csv/Agent_Detail_URL.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        browser.get(row[0])
        browser.implicitly_wait(random.randint(5,15))
        csvrecord = []
        getAgentDetail(csvrecord)
        writer.writerow(csvrecord)

browser.quit()
