from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePg:
    checkoutComplete_id = "checkout_complete_container"


def __init__(self, driver):
    self.driver = driver


def verifyCheckoutComplete(self):
    wait = WebDriverWait(self.driver, 15)
    element = wait.until(EC.element_to_be_clickable((By.ID, self.checkoutComplete_id)))
    element.is_displayed()
