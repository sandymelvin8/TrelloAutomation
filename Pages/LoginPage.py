from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from config.config import TestData
import time


class LoginPage(BasePage):

    """Object repo"""

    EMAIL = (By.ID, "user")
    PASSWORD = (By.ID, "password")
    LOGIN_WITH_ATLASSIAN = (By.ID, "login")
    LOGIN_BUTTON= (By.XPATH, "//button[@id='login-submit']")
    SUBMIT_BUTTON= (By.XPATH, "//input[@id='login']")

    """Constructor of Login page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""
    def get_login_page_title(self, title):
        return self.do_get_title(title)

    def do_valid_login(self, username, password):
        try:
            self.do_send_keys(self.EMAIL, username)
            time.sleep(2)
            self.do_click(self.LOGIN_WITH_ATLASSIAN)
            self.do_send_keys(self.PASSWORD, password)
            self.do_click(self.LOGIN_BUTTON)
            return HomePage(self.driver)
        except Exception as e:
            print(e)

    def do_invalid_login(self, username, password):
        try:
            self.do_send_keys(self.EMAIL, username)
            self.do_send_keys(self.PASSWORD, password)
            self.do_click(self.SUBMIT_BUTTON)

        except Exception as e:
            print(e)






