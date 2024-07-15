import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.loginPage import LoginPage
from Utils.readProperties import ReadConfig


class Test_001_Login:
    sauceDemoURL=ReadConfig().getSauceDemoURL()
    username=ReadConfig().getUsername()
    password=ReadConfig().getPasswo2rd()


    @pytest.mark.regression
    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self,setup):
        self.driver=setup
        self.driver.get(self.sauceDemoURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        allure.attach(self.driver.get_screenshot_as_png(),name="home page",attachment_type=AttachmentType.PNG)








        self.driver.quit()








