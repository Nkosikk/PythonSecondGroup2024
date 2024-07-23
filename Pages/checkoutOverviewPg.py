from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.readProperties import config


class CheckoutYrInfoPg:
    checkoutOverview_id = "checkout_summary_container"

    def __init__(self, driver):
        self.driver = driver

    def verifyCheckoutOverview(self):

    def verifyCheckoutInfoPg(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.checkoutOverview_id)))
        element.is_displayed()