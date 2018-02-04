#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import csv
import driver_path as chromedriver
import agent_site_url as site_url

options = webdriver.ChromeOptions()
# UAの設定
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
driver = webdriver.Chrome(chromedriver.path,chrome_options=options)

# URLを開く
driver.get(site_url.url)
driver.implicitly_wait(random.randint(5,15))

# 区分　[有料職業紹介事業] をクリック
driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphHFContent_cphContent_cbJigyoshoKbnYu"]').click()
driver.implicitly_wait(random.randint(5,15))

# 都道府県　[全国] をクリック
driver.execute_script("window.scrollTo(0, 1500);")
checkbox = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphHFContent_cphContent_cbZenkoku"]').click()
driver.implicitly_wait(random.randint(5,15))

# 検索をクリック
driver.find_element_by_xpath('//*[@id="ctl00_ctl00_cphHFContent_cphContent_btnSearch"]').click()
driver.implicitly_wait(20)

# csvファイルの生成
f = open('csv/Agent_Call_List.csv','w')
writer = csv.writer(f, lineterminator='\n')

# id名定義
idtop = 'ctl00_ctl00_cphHFContent_cphContent_repList_ctl'
seq = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20']
idend = ['_lbKyokatodokedeNo','_lbKyokatodokedeDate','_lbJigyoshoAddress','_lbTel','_lbYuryou','_lbninteiNo']

# 要素の取得
def getItems(items):
    for i in range(len(seq)):
# 事業主名、事業所名称の取得
        corp = idtop + str(seq[i]) + '_lbJigyonushiName2'
        office = idtop + str(seq[i]) + '_lbJigyoshoName2'
        corp2 = idtop + str(seq[i]) + '_lbJigyonushiName'
        office2 = idtop + str(seq[i]) + '_lbJigyoshoName'
        try:
            cp1 = driver.find_element_by_id(corp).text
            items.append(cp1.replace("\u3000"," "))
            cp2 = driver.find_element_by_id(office).text
            items.append(cp2.replace("\u3000"," "))
        except:
            cp1 = driver.find_element_by_id(corp2).text
            items.append(cp1.replace("\u3000"," "))
            cp2 = driver.find_element_by_id(office2).text
            items.append(cp2.replace("\u3000"," "))
# 受理受付年月日、所在地、電話番号、職業紹介優良事業者の取得
        for n in range(len(idend)):
            Id = idtop + str(seq[i]) + idend[n]
            item = driver.find_element_by_id(Id).text
            items.append(item.replace("\u3000"," "))
        print(items)
        writer.writerow(items)
        items = []

# クローリング
i = 0
# while i < 3:
while i < 1020:
    i = i + 1
    pagetop = 'ctl00_ctl00_cphHFContent_cphContent_repList_ctl21_pg'
    page = ['2','3','4','5','6','7','8','9','10','Next']
    for loop in range(len(page)):
        items = []
        getItems(items)
        driver.implicitly_wait(random.randint(10,30))
        Move = pagetop + str(page[loop])
        driver.execute_script("window.scrollTo(1500, document.body.scrollHeight);")
        driver.find_element_by_id(Move).click()

browser.quit()
