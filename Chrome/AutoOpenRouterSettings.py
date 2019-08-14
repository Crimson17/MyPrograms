from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(r"C:\Users\Ivan\Documents\GitHub\MyPrograms\ChromeVersions\76.exe", options=options)

browser.get(r"http://192.168.1.1")
browser.find_element_by_id("Frm_Username").send_keys("user")
browser.find_element_by_id("Frm_Password").send_keys("ZTEE40NF5L09939")
browser.find_element_by_id("LoginId").click()

