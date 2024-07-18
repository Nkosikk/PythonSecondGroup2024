from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourCartPage:
    yourCart_id = "cart_contents_container"
    checkout_button_id = "checkout"

    def __init__(self, driver):
        self.driver = driver

    def verifyYourCart(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.yourCart_id)))
        element.is_displayed()

    def clickCheckoutButton(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.checkout_button_id)))
        element.click()
