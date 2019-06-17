from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, os, sys
from easygui import *

y = 0
listOfFiles = []

if "73" in open("Readme.txt").read():
    chromeVersionNumber = 73
elif "74" in open("Readme.txt").read():
    chromeVersionNumber = 74
elif "75" in open("Readme.txt").read():
    chromeVersionNumber = 75
elif "76" in open("Readme.txt").read():
    chromeVersionNumber = 76
else:
    sys.exit("You are either using unsupported Chrome version or you have inputed the wrong number in the Readme.txt file.")

linkInput = str(input('Youtube link: '))
folderPath = diropenbox("Choose your download destination!")
folderPath = folderPath + "\YT_Download"

if not os.path.isdir(folderPath):
    os.mkdir(folderPath)

options = webdriver.ChromeOptions()
preferences = {"download.default_directory": folderPath, "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs", preferences)

browser = webdriver.Chrome(r"ChromeVersions\%d.exe" % chromeVersionNumber, options=options)
browser.get('https://ytmp3.cc/')
browser.find_element_by_id('input').send_keys(linkInput)
browser.find_element_by_id('submit').click()

try:
    while browser.find_element_by_xpath('//*[@id="download" and @href=""]'):
        print('Please wait..')
        time.sleep(1)
except NoSuchElementException:
    browser.find_element_by_id('download').click()

time.sleep(1) #Just in case it didn't start to download immediately

while y == 0:
    for r, d, f in os.walk(folderPath):
        for file in f:
            listOfFiles.append(os.path.join(r, file))
    if any("crdownload" in s for s in listOfFiles):
        time.sleep(0.5)
        listOfFiles = []
    else:
        time.sleep(0.5)
        y = 1
        print("The video has been converted.")
        browser.quit()
