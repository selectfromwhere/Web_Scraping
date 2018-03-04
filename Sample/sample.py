from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time
import csv
import re

# オプションの設定
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
options.add_argument('--blink-settings=imagesEnabled=false')

# Chromeドライバの起動
driver = webdriver.Chrome('__Path__',chrome_options=options)

# URLで指定したページに移動する
driver.get('__URL__')

# 【未実装】タイトルに"Python"があるかのアサーション(動作確認)
assert "Python" in driver.title

# 要素を取得する
# find_elements_by_ で複数要素をList型で取得
elem = driver.find_element_by_name('')
elem = driver.find_element_by_id('')
elem = driver.find_element_by_name('')
elem = driver.find_element_by_xpath('')
elem = driver.find_element_by_tag_name('')
elem = driver.find_element_by_class_name('')
elem = driver.find_element_by_css_selector('')
## 【未実装】
elem = driver.find_element_by_link_text('')
elem = driver.find_element_by_partial_link_text('')

# 要素が見つからない場合の処理
try:
    elem = driver.find_element_by_xpath('')
except NoSuchElementException:
    elem = driver.find_element_by_xpath('')

# キーボード入力
elem.send_keys("Python")

# クリック
elem.click()

# 【未実装】ドラッグ アンド ドロップ
element = driver.find_element_by_name('source')
target = driver.find_element_by_name('target')

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()

# ロードの待機
driver.implicitly_wait(__s__)
# 動作の待機
time.sleep(__s__)

# 【未実装】ブラウザの操作
driver.forward()
driver.back()

# タブを閉じる
driver.close()
# ブラウザを閉じる
driver.quit()

# 今後調べて実装
clear
send_keys(Keys.RETURN)
select
submit
switch_to_window
switch_to_frame
switch_to_default_content
switch_to_alert
add_cookie
get_cookies

## リファレンス
https://kurozumi.github.io/selenium-python/index.html
http://www.seleniumqref.com