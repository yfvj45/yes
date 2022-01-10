import time
import os
import undetected_chromedriver.v2 as uc
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = uc.ChromeOptions()
#USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
#options.add_argument('--user-agent=%s' % USER_AGENT)
options.headless=True
options.add_argument('--headless')

driver = uc.Chrome(options=options,version_main=96)

driver.get("https://temp-mail.org/en/")
print("Start")
driver.execute_script("window.open('');")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.youtube.com/")
driver.maximize_window()    
time.sleep(20)
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').click()
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("USE  unlimited internet by bypass Wifi login  break the limit.")
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]').click()
print("Started")
time.sleep(3)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.youtube.com/watch?v=KhgjRa0wli4&list=UUOsxh5uNZFWSC7aYR-vvm-A")
time.sleep(2)
driver.save_screenshot('ss.png')
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get("https://youtu.be/6G-pTxdjao4")
time.sleep(2)
driver.execute_script("window.open('');")    
driver.switch_to.window(driver.window_handles[4])
driver.get("https://youtu.be/eJeBFr4FgDI")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[5])
driver.get("https://youtu.be/1V-tQzN6Azw")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[6])
driver.get("https://youtu.be/-kSxVQghbY0")
time.sleep(2)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[7])
driver.get("https://youtu.be/h2889QVThX4")
time.sleep(2)
time.sleep(600)
print("End")

    
    
    
    
    




    
    
