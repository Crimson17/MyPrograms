from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, os, easygui

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(r"C:\Users\Ivan\Documents\GitHub\MyPrograms\ChromeVersions\75.exe", options=chrome_options)
#browser.get(r"https://www.facebook.com/")
browser.get(r"https://www.facebook.com/messages/t/crimson.ivan.9")

browser.find_element_by_id("email").send_keys("crimson6999@gmail.com")
time.sleep(0.2)
browser.find_element_by_id("pass").send_keys("justtesting")
time.sleep(0.2)
browser.find_element_by_id("loginbutton").click()
time.sleep(0.3)

message = browser.find_element_by_xpath('//*[@id="row_header_id_user:100022865750608"]/a/div/div[2]/div[2]/span/span').text

while message != "stop":
    message = browser.find_element_by_xpath('//*[@id="row_header_id_user:100022865750608"]/a/div/div[2]/div[2]/span/span').text
    print(message)
    time.sleep(1.5)

#browser.find_element_by_xpath('//*[@id="js_12"]/div').click()
#time.sleep(10)
#browser.quit()


