import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.checkoutYrInfoPg import CheckoutYrInfoPg
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.yourCartPage import YourCartPage
from Utils.readProperties import ReadConfig


class Test_Purchase_Item:
    sauceDemoURL = ReadConfig().getSauceDemoURL()
    username = ReadConfig().getUsername()
    password = ReadConfig().getPassword()
    firstName = ReadConfig().getFirstName()
    lastName = ReadConfig().getLastName()
    zipCode = ReadConfig().getZipCode()

    @pytest.mark.regression
    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_PurchaseItemTests(self, setup):
        self.driver = setup
        self.driver.get(self.sauceDemoURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login page", attachment_type=AttachmentType.PNG)
        self.lp.clickLogin()
        self.hp = HomePage(self.driver)
        self.hp.verifyBurgerMenu()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.hp.selectAddBackPack()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.hp.verifySelectedBackPack()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.hp.clickShoppingCartContainer()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home page", attachment_type=AttachmentType.PNG)
        self.yp = YourCartPage(self.driver)
        self.yp.verifyYourCart()
        allure.attach(self.driver.get_screenshot_as_png(), name="Your Cart page", attachment_type=AttachmentType.PNG)
        self.yp.clickCheckoutButton()
        self.cyi = CheckoutYrInfoPg(self.driver)
        self.cyi.verifyCheckoutInfoPg()
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout Your Info page",
                      attachment_type=AttachmentType.PNG)
        self.cyi.enterFirstName(self.firstName)
        self.cyi.enterLastName(self.lastName)
        self.cyi.enterZipCode(self.zipCode)
        allure.attach(self.driver.get_screenshot_as_png(), name="Checkout Your Info page",
                      attachment_type=AttachmentType.PNG)
        self.cyi.clickContinue()
        self.driver.quit()
