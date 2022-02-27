from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')

target_url = 'https://www.naver.com/'

driver.get(target_url) # get() 웹페이지 불러오는 구문

search_box = driver.find_element_by_name('query')

search_box.send_keys('Python') 
# 사이트 url 에서 작은따옴표로 입력하는게 일종의 약속

search_box.submit()

#종료?
# driver.close()