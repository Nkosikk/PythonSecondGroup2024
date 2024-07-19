from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.readProperties import config


class CheckoutYrInfoPg:
    checkoutYrInfo_id = "checkout_info_container"
    textbox_firstName_id = 'first-name'
    textbox_lastName_id = 'last-name'
    text_zipCode_id = 'postal-code'
    clickContinue_button_id = 'continue'

    def __init__(self, driver):
        self.driver = driver

    def verifyCheckoutInfoPg(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.checkoutYrInfo_id)))
        element.is_displayed()

    def enterFirstName(self, firstName):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_firstName_id)))
        element.send_keys(firstName)

    def enterLastName(self, lastName):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_lastName_id)))
        element.send_keys(lastName)
    def enterZipCode(self, zipCode):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.text_zipCode_id)))
        element.send_keys(zipCode)

    def clickContinue(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.clickContinue_button_id)))
        element.click()
