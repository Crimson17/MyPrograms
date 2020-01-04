import socket, time
from selenium import webdriver

myIp = socket.gethostbyname(socket.gethostname())
txtIp = open("Portforward_IP.txt").read()
i = 0

if myIp not in txtIp:
    browser = webdriver.Chrome(r"C:\Users\Ivan\Documents\GitHub\MyPrograms\ChromeVersions\78.exe")
    browser.get(r"http://192.168.1.1")
    browser.find_element_by_id("Frm_Username").send_keys("user")
    browser.find_element_by_id("Frm_Password").send_keys("ZTEE40NF5L09939")
    browser.find_element_by_id("LoginId").click()
    time.sleep(2)

    browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="mainFrame"]'))
    time.sleep(2)

    browser.find_element_by_id("mmApp").click()
    time.sleep(6)

    browser.find_element_by_id("smPForward").click()
    time.sleep(5)

    row_count = len(browser.find_elements_by_xpath("//table[@id='fwpm_Table']/tbody/tr"))

    numberOfRows = int((row_count - 2) / 2)

    for i in range(numberOfRows - 1):
        buttonIds = "modify%d" % i
        browser.find_element_by_id(buttonIds).click()
        browser.find_element_by_id("Frm_InternalHost").clear()
        browser.find_element_by_id("Frm_InternalHost").send_keys(myIp)
        browser.find_element_by_id("Btn_Edit").click()
        time.sleep(10)

    open("Portforward_IP.txt","w").write(myIp)
    time.sleep(1)
    browser.quit()
    print("You'r portforward settings have been changed!")
else:
    print("You'r ip is the same as the ones in you'r portforward settings.")




