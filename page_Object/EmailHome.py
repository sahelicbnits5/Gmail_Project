from selenium.webdriver.common.by import By

from page_Object.ComposePage import ComposePage
import time

from page_Object.Mail_Page import MailPage


class EmailHome:
    def __init__(self, driver):
        self.driver = driver

    profile_icon = (By.XPATH, "//img[@class='gb_Ca gbii']")
    popup = (By.XPATH, "//button[@class='bja J-I']")
    name = (By.XPATH, "//div[@class='znj3je NB6Lnc']")
    emailid = (By.XPATH, "//div[@class='Wdz6e ZnExKf']")
    compose_block = (By.CSS_SELECTOR, "div[class='T-I T-I-KE L3']")
    all_mail_subject = (By.CSS_SELECTOR, "tbody tr td:nth-child(4)")

    def is_popup_present(self) -> bool:
        popup = self.driver.find_elements(*EmailHome.popup)
        popup_present = False
        if len(popup) >= 1:
            print("PopUp is present")
            popup_present = True
        return popup_present

    def close_popup(self):
        self.driver.find_element(By.XPATH, "//button[@class='bja J-I']").click()

    def get_profile_icon(self):
        return self.driver.find_element(*EmailHome.profile_icon).click()

    def get_profile_name(self):
        return self.driver.find_element(*EmailHome.name)

    def get_profile_id(self):
        return self.driver.find_element(*EmailHome.emailid)

    def get_compose_block(self):
        self.driver.find_element(*EmailHome.compose_block).click()

    def compose_page(self):
        compose_page = ComposePage(self.driver)
        return compose_page

    def get_all_mail_subject(self):
        all_mails = self.driver.find_elements(*EmailHome.all_mail_subject)
        all_mails[0].click()
        mail_page = MailPage(self.driver)
        return mail_page
