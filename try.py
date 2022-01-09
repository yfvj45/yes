import time
import os
from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
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
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("2020- GOOGLE CHROME COOL INSPECT TRICKS.1% PEOPLE KNOW ABOUT THIS..")
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(Keys.ENTER)
print('Search_Start')
time.sleep(5)
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]').click()
time.sleep(8)
driver.find_element_by_css_selector('button.ytp-button.ytp-settings-button').click()
driver.find_element_by_xpath("//div[contains(text(),'Quality')]").click()
time.sleep(2)   # you can adjust this time
quality = driver.find_element_by_xpath("//span[contains(string(),'144p')]")
print("Element is visible? " + str(quality.is_displayed()))
quality.click()
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.youtube.com/watch?v=KhgjRa0wli4&list=UUOsxh5uNZFWSC7aYR-vvm-A")
time.sleep(2)
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
    
    
    
    
    




    
    
