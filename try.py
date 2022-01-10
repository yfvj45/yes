import time
import os
from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
options.add_argument('--user-agent=%s' % USER_AGENT)
options.add_argument('--headless')
options.add_argument("--no-sandbox"); # Bypass OS security model

driver = webdriver.Chrome(options=options)
print("Start")
driver.get("https://temp-mail.org/en/")
time.sleep(2)
print("temp_open")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.get("https://www.youtube.com/")
print("Youtube_Open")
driver.maximize_window()
time.sleep(20)
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').click()
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("ITAM Games Token Complete detail Review How To Buy and Sell  In Trust wallet")
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
print('Search_Start')
time.sleep(5)
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]').click()
time.sleep(3)
print("Item_Found")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.youtube.com/watch?v=KhgjRa0wli4&list=UUOsxh5uNZFWSC7aYR-vvm-A")
time.sleep(2)
print("playlist")
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get("https://youtu.be/6G-pTxdjao4")
print('Link_Play')
time.sleep(2)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[4])
driver.get("https://youtu.be/eJeBFr4FgDI")
print('Link_Play')
time.sleep(3)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[5])
driver.get("https://youtu.be/1V-tQzN6Azw")
print('Link_Play')
time.sleep(3)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[6])
driver.get("https://youtu.be/-kSxVQghbY0")
print('Link_Play')
time.sleep(3)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[7])
driver.get("https://www.youtube.com/watch?v=4xS-eMXg15E")
time.sleep(21600)
print("End")
    
    
    
    
    




    
    
