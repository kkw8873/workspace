from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) # url 로 이동

# 가는날 선택

browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 27,28일 선택
time.sleep(2) # 시발 1시간동안 찾았네 왠지는 모르겠지만 딴건 다안돼고 버튼클릭전에 time넣어주면 쌉가능 왜지..?
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button").click()
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button").click()

# 다음달 27,28일 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[1]/button").click()
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[2]/button").click()

# 이번달 27일, 다음달 28일 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[2]/button").click()

# 제주도 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button")
