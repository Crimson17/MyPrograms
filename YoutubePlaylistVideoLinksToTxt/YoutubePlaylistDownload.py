import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

playlistLInk = input("URL of the playlist: ")
numberOfVideos = int(input("Number of videos: "))

browser = webdriver.Chrome(r"C:\Users\Ivan\Documents\GitHub\MyPrograms\ChromeVersions\75.exe", options=options)
browser.get(playlistLInk)

open('Links.txt', 'w').close()

for i in range(numberOfVideos):
    file = open("Links.txt", "a")
    file.write(browser.current_url + "\n")

    time.sleep(1)

    action = ActionChains(browser)
    action.key_down(Keys.LEFT_SHIFT)
    action.key_down("n")
    action.key_up("n")
    action.key_up(Keys.LEFT_SHIFT)
    action.perform()

    time.sleep(1)

browser.quit()
