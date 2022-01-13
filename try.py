import time
import os
import undetected_chromedriver.v2 as uc
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def create_chromedriver(title,t):
    options = uc.ChromeOptions()
    options.headless=True
    options.add_argument('--headless')
    options.set_capability("detach", True)
    driver = uc.Chrome(options=options,version_main=96)
    driver.get("https://temp-mail.org/en/")
    print("Start")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.youtube.com/")
    driver.maximize_window()
    
    time.sleep(20)
    driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').click()
    driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(title)
    driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
    
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]').click()
    time.sleep(3)
    driver.save_screenshot('Video.png')
    print("Video_found")
    time.sleep(t)
    

     
  

proxies  = []
with open('p.txt') as f:
    for line in f:
        proxies.append(line)
for i in proxies:
    s=i.split(':')
    title=s[0]
    t=int(s[1].strip())
    print(title,t)
    create_chromedriver(title,t)
    

    
    
