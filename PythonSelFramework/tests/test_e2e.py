from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()    # this method returns object of next class
        log.info("Getting all the card titles")
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooters()[i].click()

        checkoutPage.getButtonPrimary().click()

        confirmPage = checkoutPage.getCheckOutItems()
        log.info("Entering country name as 'un'")
        confirmPage.getCountry().send_keys("un")
        self.verifyLinkPresence("United States of America")

        confirmPage.getDesiredCountry().click()
        confirmPage.getCheckBoxPrimary().click()
        confirmPage.getSubmitButton().click()
        textMatch = confirmPage.getAlertSuccess().text
        log.info("Text received from application is " + textMatch)

        assert ("Success! Thank you!" in textMatch)



