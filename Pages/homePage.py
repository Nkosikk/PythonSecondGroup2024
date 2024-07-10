from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    burgemenu = 'react-burger-menu-btn'

    def __init__(self, driver):
        self.driver = driver

    def verifyBurgerMenu(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.presence_of_element_located(By.ID, self.burgemenu))
        element.is_displayed()


