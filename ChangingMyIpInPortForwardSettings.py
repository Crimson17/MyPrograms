import socket, time
from selenium import webdriver

myIp = socket.gethostbyname(socket.gethostname())
txtIp = open("Portforward_IP.txt").read()

if myIp not in txtIp:
    browser = webdriver.Chrome(r"C:\Users\Ivan\Documents\GitHub\MyPrograms\ChromeVersions\75.exe")
    browser.get(r"http://192.168.1.1")
    browser.find_element_by_id("Frm_Username").send_keys("user")
    browser.find_element_by_id("Frm_Password").send_keys("ZTEE40NF5L09939")
    browser.find_element_by_id("LoginId").click()
    browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="mainFrame"]'))
    browser.find_element_by_id("mmApp").click()
    browser.find_element_by_id("smPForward").click()
    for i in range(4):
        buttonIds = "modify%d" % i
        time.sleep(1)
        browser.find_element_by_id(buttonIds).click()
        browser.find_element_by_id("Frm_InternalHost").clear()
        browser.find_element_by_id("Frm_InternalHost").send_keys(myIp)
        browser.find_element_by_id("Btn_Edit").click()
    open("Portforward_IP.txt","w").write(myIp)
    time.sleep(1)
    browser.quit()
    print("You'r portforward settings have been changed!")
else:
    print("You'r ip is the same as the ones in you'r portforward settings.")





