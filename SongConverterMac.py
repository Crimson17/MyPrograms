from selenium import webdriver


linkInput = str(input('Unesite Youtube link: '))
odbariFormata = int(input('Samo zvuk?(0) ili video?(1) '))

if odbariFormata == 1:
    print('wip')
else:
    browser = webdriver.Chrome('/Users/ivanperanovic/Documents/Webdriver/chromedriver')
    browser.get('https://www.onlinevideoconverter.com/mp3-converter')
    browser.find_element_by_id('texturl').send_keys(linkInput)
    browser.find_element_by_id('convert1').click()



