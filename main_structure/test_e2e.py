import time

from selenium.webdriver import Keys

from page_Object.ComposePage import ComposePage
from page_Object.EmailHome import EmailHome
from page_Object.LoginPage import LoginPage
from page_Object.Mail_Page import MailPage
from page_Object.Send_Page import SentPage
from utilities.BaseClass import BaseClass


class TestMain(BaseClass):

    def test_gmail(self, get_username):

        self.driver.implicitly_wait(10)

        login_page = LoginPage(self.driver)
        login_page.get_mailid_input().send_keys(get_username)
        self.element_wait_clickable(login_page.get_id_next_btn())
        login_page.get_id_next_btn().click()
        time.sleep(5)
        login_page.get_pass_input().send_keys("cbnits@1234")
        self.element_wait_clickable(login_page.pass_next_btn)
        homepage = login_page.get_pass_next_btn()
        time.sleep(2)
        email_page = EmailHome(self.driver)
        pop_up = email_page.is_popup_present()
        if pop_up:
            print("close popup")
            email_page.close_popup()
        # breakpoint()
        self.element_wait_presence(email_page.profile_icon)
        email_page.get_profile_icon()
        breakpoint()
        self.driver.switch_to.frame('account')
        time.sleep(3)
        self.element_wait_presence(EmailHome.name)
        assert email_page.get_profile_name().text == "Saheli Saheli"

        self.element_wait_presence(email_page.emailid)
        assert email_page.get_profile_id().text == "saheli.mondal@fedev.cbnits.com"

        self.driver.switch_to.default_content()
        self.element_wait_clickable(email_page.compose_block)
        email_page.get_compose_block()
        compose_page = email_page.compose_page()
        # time.sleep(12)
        breakpoint()
        self.element_wait_presence(ComposePage.max)
        compose_page.get_max()

        self.element_wait_presence(ComposePage.subject)
        compose_page.get_subject_input()

        self.element_wait_presence(ComposePage.body)
        for i in range(0, 50):
            compose_page.get_body_input()

        # breakpoint()
        time.sleep(5)
        self.element_wait_presence(ComposePage.input_area)
        compose_page.get_to_input()

        self.element_wait_clickable(ComposePage.send)
        compose_page.get_send_btn()

        sent_page = compose_page.sent_page()

        time.sleep(5)

        self.element_wait_clickable(SentPage.sent_btn)
        sent_page.get_sent_btn().click()

        self.element_wait_presence(SentPage.sent_mails)
        sent_mails = sent_page.get_sent_mails()

        time.sleep(2)

        self.element_wait_presence(SentPage.sent_mails)

        time.sleep(5)

        sent_mails[0].click()

        self.element_wait_clickable(SentPage.inbox_btn)
        sent_page.get_inbox_btn().click()

        self.element_wait_presence(EmailHome.all_mail_subject)
        mailpage = sent_page.get_all_mail_subject()

        self.element_wait_presence(MailPage.rec_mail_subject)
        rec_mail_subject1 = mailpage.get_rec_mail_subject().text
        print(rec_mail_subject1)

        assert rec_mail_subject1 == 'Hello'

        self.element_wait_clickable(MailPage.dot_option)
        mailpage.get_dot_option().click()

        self.element_wait_clickable(MailPage.reply_option)
        mailpage.get_reply_option().click()

        self.element_wait_clickable(MailPage.discard_btn)
        mailpage.get_discard_btn().click()

        self.element_wait_clickable(EmailHome.profile_icon)
        homepage.get_profile_btn().click()

        self.driver.switch_to.frame('account')

        self.element_wait_clickable(MailPage.sign_out_btn)
        google_page = mailpage.get_sign_out_btn()
        self.driver.switch_to.default_content()

        self.driver.get('https://www.google.com/')

        sign_in_text = google_page.get_sign_out().text

        assert sign_in_text == 'Sign in'
