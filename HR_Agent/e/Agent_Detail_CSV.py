#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import csv
import random
import driver_path as chromedriver

def getAgentDetail(csvrecord):
    dic = {}

    corp = browser.find_element_by_class_name('companyName').text
    dic.setdefault('社名',corp)
    print(dic['社名'])

    items = browser.find_elements_by_class_name('dataSetTable')
    item = items[0].find_elements_by_class_name('dataSet')
    for a in range(len(item)):
        text = item[a].find_element_by_class_name('text').text
        data = item[a].find_elements_by_class_name('setData')
        for n in range(len(data)):
            if n == 0:
                xxx = data[n].text
            else:
                xxx = xxx + ' / ' + data[n].text
        dic.setdefault(text,xxx)


    item = items[1].find_elements_by_class_name('dataSet')
    for a in range(len(item)):
        text = item[a].find_element_by_class_name('text').text
        xxx = item[a].find_element_by_class_name('data').text.replace("\n"," ")
        dic.setdefault(text,xxx)


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

f = open('csv/Agent_Detail.csv','w')
writer = csv.writer(f, lineterminator='\n')
header = ['社名','紹介事業事業所','設立','従業員数','厚生労働大臣許可番号','紹介事業許可年','ホームページ','業種','職種']
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
