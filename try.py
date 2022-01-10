import time
import os
from selenium import webdriver
import undetected_chromedriver.v2 as uc
import threading

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()
options = uc.ChromeOptions()
#USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
#options.add_argument('--user-agent=%s' % USER_AGENT)
#options.headless=True
#options.add_argument('--headless')
options.add_argument("--no-sandbox"); # Bypass OS security model

driver = uc.Chrome(options=options,version_main=96)
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
time.sleep(3)
print("playlist")
driver = uc.Chrome(options=options,version_main=96)
driver.get("https://youtu.be/6G-pTxdjao4")
print('Link_Play')
time.sleep(3)
driver = uc.Chrome(options=options,version_main=96)
driver.get("https://youtu.be/eJeBFr4FgDI")
print('Link_Play')
time.sleep(3)
driver = uc.Chrome(options=options,version_main=96)
driver.get("https://youtu.be/1V-tQzN6Azw")
print('Link_Play')
time.sleep(3)
driver = uc.Chrome(options=options,version_main=96)
driver.get("https://youtu.be/-kSxVQghbY0")
print('Link_Play')
time.sleep(3)
driver = uc.Chrome(options=options,version_main=96)
driver.get("https://www.youtube.com/watch?v=4xS-eMXg15E")
time.sleep(600)
print("End")
vdisplay.stop()
    
    
    
    
    




    
    
