from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.readProperties import config


class CheckoutOverviewPg:
    checkoutOverview_id = "checkout_summary_container"
    finishButton_id = "finish"

    def __init__(self, driver):
        self.driver = driver

    def verifyCheckoutOverview(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.checkoutOverview_id)))
        element.is_displayed()
    def clickFinishButton(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID , self.finishButton_id)))
        element.click()
