from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutOverviewPage:

    overviewPageTitle = "//span[@class='title'][contains(.,'Checkout: Overview')]"
    cartList = "cart_list"
    cartItem = "cart_item"
    subTotalLbl = "//div[contains(@class,'summary_subtotal_label')]"
    taxLbl = "//div[contains(@class,'summary_tax_label')]"
    totalLbl = "//div[contains(@class,'summary_total_label')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyOnProductOverviewPage(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.overviewPageTitle)))

    def calculateCartItems(self):
        wait = WebDriverWait(self.driver, 15)
        cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, self.cartList)))
        items = cart.find_elements(By.CLASS_NAME, self.cartItem)
        if items.__len__() > 0:
            sub = float(cart.find_element(By.XPATH, self.subTotalLbl).text.split(" ")[2].split("$")[1])
            #tax = float(cart.find_element(By.XPATH, self.taxLbl).text.split(" ")[1].split("$")[1])
            tot = float(cart.find_element(By.XPATH, self.totalLbl).text.split(" ")[1].split("$")[1])
            print(tot)
            taxPerc = 0.08
            taxAmount = sub * taxPerc
            tempTot = sub + taxAmount
            if float(tempTot.__format__(".2f")) == tot:
                assert True
            else:
                assert False
        else:
            print()