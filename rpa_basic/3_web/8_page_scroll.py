from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://shopping.naver.com/home/p/index.naver')

# 무선 마우스 입력
elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys("무선마우스")

time.sleep(1)

elem.send_keys(Keys.ENTER)

# 스크롤
# 지정한 위치로 스크로 내리기
# browser.execute_script("window.scrollTo(0, 1080)")
# 싹다 내리기
interval = 2
prev_scroll = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)

    curr_scroll = browser.execute_script("return document.body.scrollHeight")
    if curr_scroll == prev_scroll:
        break
    prev_scroll = curr_scroll

browser.execute_script("window.scrollTo(0, 0)")



time.sleep(5)
browser.quit()