import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Pages.cartPage import CartPage
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.CheckoutPage import CheckoutPage
from Utils.readProperties import ReadConfig


class Test_001_Login:
    sauceDemoURL = ReadConfig().getSauceDemoURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getPasswo2rd()
    firstName = ReadConfig().getFirstName()
    lastName = ReadConfig().getLastName()
    ZipCode = ReadConfig().getZipCode()

    @pytest.mark.regression
    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self, setup):
        self.driver = setup
        self.driver.get(self.sauceDemoURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.cp = CartPage(self.driver)
        self.ck = CheckoutPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login page", attachment_type=AttachmentType.PNG)
        self.lp.clickLogin()
        self.hp.verifyBurgerMenu()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.hp.selectBAckPack()
        allure.attach(self.driver.get_screenshot_as_png(), name="item added to cart",
                      attachment_type=AttachmentType.PNG)
        self.hp.verifyRemoveIdDisplayed()
        self.hp.clickCart()
        allure.attach(self.driver.get_screenshot_as_png(), name="cart page screen",
                      attachment_type=AttachmentType.PNG)
        self.cp.verifyYourCartTitleIsDisplayed()
        self.cp.clickCheckoutButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="checkout screen",
                      attachment_type=AttachmentType.PNG)
        self.ck.setFirstName(self.firstName)
        self.ck.setLastName(self.lastName)
        self.ck.setPostalCode(self.ZipCode)

        self.driver.quit()
