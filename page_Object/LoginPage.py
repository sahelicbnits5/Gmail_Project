from selenium.webdriver.common.by import By
from page_Object.EmailHome import EmailHome
from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    mailId_input = (By.XPATH, "//*[@id='identifierId']")
    id_nxt_btn = (By.XPATH, "//div[@id='identifierNext']")
    pass_input = (By.XPATH, "//input[@aria-label='Enter your password']")
    pass_next_btn = (By.XPATH, "//div[@id='passwordNext']")

    def get_pass_next_btn(self):
        self.driver.find_element(*LoginPage.pass_next_btn).click()

    def get_mailid_input(self):
        return self.driver.find_element(*LoginPage.mailId_input)

    def get_id_next_btn(self):
        return self.driver.find_element(*LoginPage.id_nxt_btn)

    def get_pass_input(self):
        return self.driver.find_element(*LoginPage.pass_input)

