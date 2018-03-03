#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import scraping_info as s_inf

# 企業詳細を開く
browser.get(s_inf.targets['y'])
# 入社理由とギャップ
r_n_g = browser.find_elements_by_class_name('questionList_item')
r_n_g[2].click()

# エンジニア職
engineer = browser.find_elements_by_class_name('button button-refine fs-12')
engineer[1].click()

# 回答日が新しい順
ans_date = browser.find_elements_by_class_name('sortTab_item')
ans_date[0].click()

# コメントの取得
comments = browser.find_elements_by_class_name('article_answer')
for i in range(25):
    print(comments[i].text)


# csvファイルの生成
f = open('csv/Company_reviews.csv','w')
writer = csv.writer(f, lineterminator='\n')