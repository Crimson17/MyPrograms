from selenium import webdriver


linkInput = str(input('Unesite Youtube link: '))
odbariFormata = int(input('Samo zvuk?(0) ili video?(1) '))

if odbariFormata == 0:

    kvalitetaZvuka = int(input('Kvaliteta zvuka?: 320, 192 ili 96?: '))

    browser = webdriver.Chrome('/Users/ivanperanovic/Documents/Webdriver/chromedriver')
    browser.get('https://www.onlinevideoconverter.com/mp3-converter')
    browser.find_element_by_id('advanced-options-link').click()
    browser.find_element_by_id('audioBitrate').click()

    if kvalitetaZvuka != 192:
        if kvalitetaZvuka == 320:
            browser.find_element_by_xpath('//a[@data-value="320"]').click()
        elif kvalitetaZvuka == 96:
            browser.find_element_by_xpath('//a[@data-value="96"]').click()
        else:
            print('Odabir kvalitete nije tocan.')

browser.find_element_by_id('texturl').send_keys(linkInput)

