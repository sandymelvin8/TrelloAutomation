import pytest
from config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
import allure
from datetime import datetime


@allure.severity(allure.severity_level.CRITICAL)
class Test_Login(BaseTest):

    @allure.severity(allure.severity_level.MINOR)
    def test_page_title(self):
        try:
            self.loginpage = LoginPage(self.driver)
            title = self.loginpage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
            assert title == TestData.LOGIN_PAGE_TITLE, "Title does not match"

        except Exception as e:
            print("Exception occurred ", e)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        try:
            self.loginpage = LoginPage(self.driver)
            self.loginpage.do_valid_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
        except Exception as e:
            print("Exception occurred ", e)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_login(self):
        try:
            self.loginpage = LoginPage(self.driver)
            self.loginpage.do_invalid_login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
            error_msg = self.driver.find_element_by_xpath("//p[@class='error-message' and contains(text(),"
                                                          "'Incorrect email address and ')]")
            assert error_msg == TestData.ERROR_MESSAGE, "Error message does not match"

        except Exception as e:
            print("Exception occurred ", e)
            current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name = "test_invalid_login" + "_screenshot_" + current_time

            # save screenshot in screenshots folder
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("C:/Users/Melvin/PycharmProjects/TrelloAutomation/Tests/screenshots/" +
                                               screenshot_name+".png")
            raise
