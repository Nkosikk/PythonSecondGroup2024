import os
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    downloadFilePath = os.getcwd() + '\\Recon\\'
    params = {'behavior': 'allow', 'downloadPath': downloadFilePath}
    driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
