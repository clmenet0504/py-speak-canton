from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
import urllib

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1020,945')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options)


# driver = webdriver.Chrome()


def wordToPhonic(word):
    print('Word (字) : ' + word)

    # url-encode the word
    word = urllib.parse.quote_plus(word)

    # preparing the link for scrapping
    link = 'https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/search.php?word=' + word

    driver.implicitly_wait(0.5)
    driver.get(link)

    # Get the phonetic of the word
    ph_initial = driver.find_element_by_xpath("//span[@id='phonetic_81']//span[@class='ph_initial']").get_attribute('innerHTML')
    ph_final = driver.find_element_by_xpath("//span[@id='phonetic_81']//span[@class='ph_final']").get_attribute('innerHTML')
    ph_tone = driver.find_element_by_xpath("//span[@id='phonetic_81']//span[@class='ph_tone']").get_attribute('innerHTML')

    print('Initial(聲母) : ' + ph_initial)
    print('Final(韻母) : ' + ph_final)
    print('Tone(音調) : ' + ph_tone)

    driver.close()


