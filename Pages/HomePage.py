from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):

    """Object repo for Home Page"""

    BOARDS_BUTTON = (By.XPATH, "//span[@class='MEu8ZECLGMLeab']")
    NEW_BOARD_BUTTON = (By.XPATH, "//button[contains(text(),'Create new board…')]")
    ADD_BOARD_TITLE = (By.XPATH, "//input[@placeholder='Add board title']")
    CREATE_BOARD_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(),'Create Board')]")

    """Constructor of Home Page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def create_new_board(self, boardname):
        try:
            time.sleep(5)
            self.do_click(self.BOARDS_BUTTON)
            time.sleep(3)
            self.do_click(self.NEW_BOARD_BUTTON)
            time.sleep(3)
            self.do_send_keys(self.ADD_BOARD_TITLE, boardname)
            # time.sleep(5)
            self.do_click(self.CREATE_BOARD_BUTTON)

        except Exception as e:
            print(e)

