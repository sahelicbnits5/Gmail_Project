from selenium.webdriver.common.by import By

from page_Object.Google_page import GooglePage


class MailPage:
    def __init__(self, driver):
        self.driver = driver

    rec_mail_subject = (By.CSS_SELECTOR, "div[class='ha'] h2")
    dot_option = (By.CSS_SELECTOR, "div[class='T-I J-J5-Ji T-I-Js-Gs aap T-I-awG T-I-ax7 L3']")
    reply_option = (By.CSS_SELECTOR, "div[class='b7 J-M'] div:nth-child(1) div div div")
    discard_btn = (By.CSS_SELECTOR, "div[class='og T-I-J3'")
    sign_out_btn = (By.CSS_SELECTOR, ".T6SHIc a .SedFmc")

    def get_rec_mail_subject(self):
        return self.driver.find_element(*MailPage.rec_mail_subject)

    def get_dot_option(self):
        return self.driver.find_element(*MailPage.dot_option)

    def get_reply_option(self):
        return self.driver.find_element(*MailPage.reply_option)

    def get_discard_btn(self):
        return self.driver.find_element(*MailPage.discard_btn)

    def get_sign_out_btn(self):
        self.driver.find_element(*MailPage.sign_out_btn).click()
        google_page = GooglePage(self.driver)
        return google_page
