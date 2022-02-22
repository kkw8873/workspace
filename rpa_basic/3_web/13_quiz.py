import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.w3schools.com/")
time.sleep(1)
browser.find_element_by_link_text("Learn HTML").click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
time.sleep(1)
browser.find_element_by_link_text("Contact Form").click()
FirstName = "나도"
LastName = "코딩"
Country = "Canada"
Subject = "퀴즈 완료하였습니다."
browser.find_element_by_xpath('//*[@id="fname"]').send_keys(FirstName)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(LastName)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="country"]').send_keys(Country)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(Subject)
time.sleep(5)
browser.find_element_by_link_text("Submit").click()
time.sleep(5)
browser.quit()


