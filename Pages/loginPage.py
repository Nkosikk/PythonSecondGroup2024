from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_username_id = 'user-name'
    textbox_password_id = 'password'

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_username_id)))
        element.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_password_id)))
        element.send_keys(password)

    # ToDo Allettah create the method to enter password
    # ToDo Zwai create the methood to click login button
    # ToDo MakMore create the methood to validate that you are in homepage



