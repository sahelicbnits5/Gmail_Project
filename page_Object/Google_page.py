from selenium.webdriver.common.by import By


class GooglePage:

    def __init__(self, driver):
        self.driver = driver

    sign_out = (By.XPATH, "//*[@id='gb']/div/div[2]/a")

    def get_sign_out(self):
        return self.driver.find_element(*GooglePage.sign_out)
