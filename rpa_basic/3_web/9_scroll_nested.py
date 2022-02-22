import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()
time.sleep(3)

# 특정 영역 스크롤

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

# 방법 1:ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법2 : 좌표 정보 이용
# xy = elem.location_once_scrolled_into_view # 함수가 아니니까() 쓰지 말기
# print("type : ", type(xy)) # dict
# print("value : ", xy)

elem.click()



time.sleep(3)
browser.quit()