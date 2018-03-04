#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import csv
import random
import time
import re
import scraping_info as s_inf

# ログイン
def Login():
    browser.get(s_inf.url)
    browser.implicitly_wait(5)
    browser.find_element_by_name('_username').send_keys(s_inf.user_name)
    browser.find_element_by_name('_password').send_keys(s_inf.password)
    browser.find_element_by_id('log_in').click()
    browser.implicitly_wait(5)

# 企業詳細を開く
def openCOpage(co):
    browser.get(s_inf.targets[co])
    browser.implicitly_wait(5)

# 企業名とレートを取得
def getCoInfo():
    co_name = browser.find_element_by_id('mainTitle').text
    co_rate = browser.find_element_by_class_name('contentsHeader_rating').text
    co_rank = browser.find_element_by_xpath('//*[@id="contentsHeader_text"]/ul/li[5]/a/span').text
    print('Company:{0} Rate({1}) Rank({2})'.format(co_name, co_rate, (re.search('\d+',co_rank)).group()))

# カテゴリの取得
def getCategory():
    time.sleep(random.randint(5,25))
    items = browser.find_elements_by_class_name('questionList_item')
    for i in range(len(items)):
        print('Category[{0}]：{1}'.format(i, items[i].text))

# カテゴリの移動
def changeCategory(ctgry):
    time.sleep(random.randint(5,25))
    browser.find_elements_by_class_name('questionList_item')[ctgry].click()

# エンジニア職の選択、回答日順に並べ替え
def fill_n_sort():
    time.sleep(random.randint(1,3))
    browser.find_element_by_xpath('//*[@id="anchor01"]/dl[1]/dd/ul/li[2]/a').click()
    browser.find_elements_by_class_name('sortTab_item')[0].click()

# コメントの取得
def getReview():
    comments = browser.find_elements_by_class_name('article_answer')
    for i in range(len(comments)):
        time.sleep(random.randint(1,5))
        print(comments[i].text)

# csvファイルの生成
def makeCSVfile():
    f = open('csv/Company_reviews.csv','w')
    writer = csv.writer(f, lineterminator='\n')


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
    browser = webdriver.Chrome(s_inf.path_biz,chrome_options=options)
    Login()
    for co in range(len(s_inf.targets)):
        openCOpage(co)
        getCoInfo()
        getCategory()
        for ctgry in range(0,9):
            changeCategory(ctgry)
            fill_n_sort()
            getReview()
    browser.close()
