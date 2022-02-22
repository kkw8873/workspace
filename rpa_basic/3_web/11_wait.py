import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://flight.naver.com/")

# 가는 날
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

time.sleep(2)
browser.find_elements_by_class_name('sc-crzoAE hnpClg inner')[20].click()

# 오는 날
# browser.find_elements_by_link_text('5')[1].click()

# # 가는 곳 
# time.sleep(1)
# browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
# browser.find_element_by_link_text("국내").click()
# browser.find_element_by_link_text("제주").click()
# browser.find_element_by_link_text("항공권 검색").click()


# try:
    #elem = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath 경로)))








time.sleep(3)
browser.quit()

