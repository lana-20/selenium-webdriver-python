from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.CSS_SELECTOR, ".card-title a")
    cardFooters = (By.CSS_SELECTOR, ".card-footer button")
    buttonPrimary = (By.CSS_SELECTOR, "a[class*=btn-primary]")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckoutPage.cardFooters)

    def getButtonPrimary(self):
        return self.driver.find_element(*CheckoutPage.buttonPrimary)

    def getCheckOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
