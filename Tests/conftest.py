import time

from selenium import webdriver


def setup(browser):
    if browser.lower() or browser.upper() == 'chrome':
        driver = webdriver.Chrome()
        time.sleep(2)

    elif browser.lower() or browser.upper() == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()

    return  driver

setup('chrome')
