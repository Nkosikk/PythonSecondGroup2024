import allure
import pytest

from Utils.readProperties import ReadConfig


class Test_001_Login:
    sauceDemoURL=ReadConfig().getSauceDemoURL()


    @pytest.mark.regression
    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self,setup):
        self.driver=setup
        self.driver.get(self.sauceDemoURL)







