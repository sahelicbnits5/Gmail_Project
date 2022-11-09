from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page_Object.Send_Page import SentPage


# from page_object.sent_page import SentPage


class ComposePage:

    def __init__(self, driver):
        self.driver = driver

    # input_area = (By.CSS_SELECTOR, "div[class='wO nr l1'] textarea")
    input_area = (By.CSS_SELECTOR, "div[aria-label='To'] input")
    # input_area = (By.CSS_SELECTOR, "div[aria - label='To']")
    max = (By.XPATH, "//td[@class='Hm']/img[@class='Hq aUG']")
    subject = (By.CSS_SELECTOR, "input[class='aoT']")
    body = (By.CSS_SELECTOR, "div[class='Am Al editable LW-avf tS-tW']")
    send = (By.CSS_SELECTOR, "div[class='T-I J-J5-Ji aoO v7 T-I-atl L3']")

    def get_max(self):
        return self.driver.find_element(*ComposePage.max).click()

    def get_to_input(self):
        return self.driver.find_element(*ComposePage.input_area)

    def get_subject_input(self):
        return self.driver.find_element(*ComposePage.subject).send_keys("Hello")

    def get_body_input(self, text):
        return self.driver.find_element(*ComposePage.body).send_keys(text)

    def get_send_btn(self):
        self.driver.find_element(*ComposePage.send).click()

    def sent_page(self):
        sent_page1 = SentPage(self.driver)
        return sent_page1
