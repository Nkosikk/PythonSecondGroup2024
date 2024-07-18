from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    burgerMenu_id = "react-burger-menu-btn"
    addBackPack_id = "add-to-cart-sauce-labs-backpack"

    def __init__(self, driver):
        self.driver = driver
    def verifyBurgerMenu(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.burgerMenu_id)))
        element.is_displayed()
    def selectBackPack(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.addBackPack_id)))
        element.click()


