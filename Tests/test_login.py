import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Utils.readProperties import ReadConfig


class Test_001_Login:
    sauceDemoURL = ReadConfig().getSauceDemoURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getPassword()

    @pytest.mark.regression
    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self, setup):
        self.driver = setup
        self.driver.get(self.sauceDemoURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login page", attachment_type=AttachmentType.PNG)
        self.lp.clickLogin()
        self.hp = HomePage(self.driver)
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.hp.verifyBurgerMenu()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.hp.selectAddBackPack()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.hp.verifySelectedBackPack()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.driver.quit()
