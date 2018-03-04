#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import re
import scraping_info as s_inf

# 企業詳細を開く
browser.get(s_inf.targets['y'])

# 企業名とレートを取得
co_name = browser.find_element_by_id('mainTitle').text
co_rate = browser.find_element_by_class_name('contentsHeader_rating').text
co_rank = browser.find_element_by_xpath('//*[@id="contentsHeader_text"]/ul/li[5]/a/span').text
print('Company:{0} Rate({1}) Rank({2})'.format(co_name, co_rate, (re.search('\d+',co_rank)).group()))

# カテゴリの取得
items = browser.find_elements_by_class_name('questionList_item')
for i in range(len(items)):
    print('Category[{0}]：{1}'.format(i, items[i].text))

# カテゴリの移動
def changeCategory(ctgry):
    browser.find_elements_by_class_name('questionList_item')[ctgry].click()

# エンジニア職の選択、回答日順に並べ替え
def fill_n_sort():
    browser.find_element_by_xpath('//*[@id="anchor01"]/dl[1]/dd/ul/li[2]/a').click()
    browser.find_elements_by_class_name('sortTab_item')[0].click()

# コメントの取得
def getReview():
    comments = browser.find_elements_by_class_name('article_answer')
    for i in range(len(comments)):
        print(comments[i].text)


# csvファイルの生成
f = open('csv/Company_reviews.csv','w')
writer = csv.writer(f, lineterminator='\n'