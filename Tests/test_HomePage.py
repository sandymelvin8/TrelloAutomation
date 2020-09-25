from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from config.config import TestData
import allure


@allure.severity(allure.severity_level.CRITICAL)
class Test_Home(BaseTest):

    def test_check_home_icon(self):
        try:
            self.loginpage = LoginPage(self.driver)
            self.homepage = HomePage(self.driver)
            self.loginpage.do_valid_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label='HouseIcon']")))
            found = True

        except NoSuchElementException:
            found = False

        assert found


    def test_create_new_board(self):
        try:
            self.loginpage = LoginPage(self.driver)
            self.homepage = HomePage(self.driver)
            self.loginpage.do_valid_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
            self.homepage.create_new_board(TestData.BOARD_NAME)
        except Exception as e:
            print("Exception occurred ", e)
            current_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name = "test_create_new_board" + "_screenshot_" + current_time
            # save screenshot in allure
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("C:/Users/Melvin/PycharmProjects/TrelloAutomation/Tests/screenshots/" +
                                               screenshot_name+".png")
            raise


