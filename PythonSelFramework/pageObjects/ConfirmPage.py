from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.ID, "country")
    country = (By.ID, "country")
    #  driver.find_element(By.LINK_TEXT, "United States of America")
    desiredCountry = (By.LINK_TEXT, "United States of America")
    #  driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    checkboxPrimary = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    #  driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton = (By.CSS_SELECTOR, "[type='submit']")
    #  driver.find_element(By.CLASS_NAME, "alert-success")
    alertSuccess = (By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getDesiredCountry(self):
        return self.driver.find_element(*ConfirmPage.desiredCountry)

    def getCheckBoxPrimary(self):
        return self.driver.find_element(*ConfirmPage.checkboxPrimary)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getAlertSuccess(self):
        return self.driver.find_element(*ConfirmPage.alertSuccess)