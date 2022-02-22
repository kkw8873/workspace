from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://naver.com")

elem = browser.find_element_by_tag_name("a")
elem
print(elem.get_attribute("href"))
