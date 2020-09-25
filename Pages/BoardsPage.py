from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


from config.config import TestData


class BoardsPage(BasePage):

    """Object repo for Boards Page"""
    BOARDS_BUTTON = (By.XPATH, "//span[@class='MEu8ZECLGMLeab']")
    SEARCH_TEXT = (By.XPATH, "//input[@name='search-boards']")
    ADD_LIST = (By.XPATH, "//span[contains(text(),'Add a list')]")
    LIST_NAME = (By.XPATH, "//input[@name='name']")
    ADD_LIST_BUTTON = (By.XPATH, "//input[@type='submit']")
    ADD_CARD1_NAME = (By.XPATH, "//span[contains(text(),'Add a card')]")
    TEXT_AREA = (By.XPATH, "//textarea[@placeholder='Enter a title for this card…']")
    EMPTY_CLICK = (By.XPATH, "//div[@id='trello-root']")
    CARD_1 = (By.XPATH, "//span[contains(text(),'card 1')]")
    CARD_2 = (By.XPATH, "//span[contains(text(),'Card 2')]")
    CARD_2_TARGET = (By.XPATH, "//textarea[contains(text(),'In Progress')]")
    CARD_3 = (By.XPATH, "//span[contains(text(),'Card 3')]")
    CARD_3_TARGET = (By.XPATH, "//textarea[contains(text(),'QA')]")
    SAVE_COMMENT_BUTTON = (By.XPATH, "//div[@class='comment-controls u-clearfix']//input[@value='Save']")
    CLOSE_COMMENT_MODAL = (By.XPATH, "//a[@class='icon-md icon-close dialog-close-button js-close-window']")


    """Constructor of Home Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def get_boards_page_title(self, title):
        return self.do_get_title(title)

    def search_board(self, boardname):
        time.sleep(10)
        self.do_click(self.BOARDS_BUTTON)
        self.do_send_keys(self.SEARCH_TEXT, boardname)
        self.send_keys_enter(self.SEARCH_TEXT)

    def create_Not_Started(self):
        self.do_click(self.ADD_LIST)
        self.do_send_keys(self.LIST_NAME, "Not started")
        time.sleep(1)
        self.do_click(self.ADD_LIST_BUTTON)

    def create_In_Progress(self):
        time.sleep(2)
        self.do_send_keys(self.LIST_NAME, "In Progress")
        time.sleep(1)
        self.do_click(self.ADD_LIST_BUTTON)

    def create_QA(self):

        time.sleep(2)
        self.do_send_keys(self.LIST_NAME, "QA")
        time.sleep(1)
        self.do_click(self.ADD_LIST_BUTTON)

    def create_Done(self):
        time.sleep(2)
        self.do_send_keys(self.LIST_NAME, "Done")
        time.sleep(1)
        self.do_click(self.ADD_LIST_BUTTON)

    def add_Cards_in_NotStarted(self):
        """Add card 1"""
        self.do_click(self.ADD_CARD1_NAME)
        self.do_send_keys(self.TEXT_AREA, "Card 1")
        self.send_keys_enter(self.TEXT_AREA)
        """Add card 2"""
        self.do_send_keys(self.TEXT_AREA, "Card 2")
        self.send_keys_enter(self.TEXT_AREA)
        """Add card 3"""
        self.do_send_keys(self.TEXT_AREA, "Card 3")
        self.send_keys_enter(self.TEXT_AREA)
        """Add card 4"""
        self.do_send_keys(self.TEXT_AREA, "Card 4")
        self.send_keys_enter(self.TEXT_AREA)
        # self.do_click(self.EMPTY_CLICK)

    def move_Card2_to_InProgress(self):
        # try:
        #     element = By.XPATH("//span[contains(text(),'Card 2')]")
        #     target = By.XPATH("//textarea[contains(text(),'In Progress')]")
        #     # self.do_mouse_hover(self.CARD_2, element)
        #     ActionChains(self.driver).drag_and_drop(element, target).perform()
        #
        #
        # except Exception as e:
        #     print(e.__traceback__, "Error occured")

        self.do_drag_and_drop(self,self.CARD_2, self.CARD_2_TARGET)

    def move_Card3_to_QA(self):
        self.do_drag_and_drop(self,self.CARD_3,self.CARD_3_TARGET)


    def move_Card2_to_QA(self):
        self.do_drag_and_drop(self,self.CARD_2,self.CARD_3_TARGET)

    def assign_Card1_to_CurrentUser(self, name):
        self.do_click(self.CARD_1)
        time.sleep(3)
        members = self.driver.find_element_by_xpath("//div[@class='window-sidebar']//span[contains(text(),'Members')]")
        members.click()
        element1 = self.driver.find_element_by_xpath("//span[@class='full-name' and contains(text(),'"+name+"')]")
        self.do_mouse_hover(self, element1)
        time.sleep(2)
        comment_box = self.driver.find_element_by_xpath("//form//div[@class='comment-box']")
        self.do_click(comment_box)
        comment = self.driver.find_element_by_xpath("//textarea[@placeholder='Write a comment…']")
        self.do_send_keys(comment, " I am Done")
        comment.search_board.send_keys(Keys.ENTER)
        self.do_click(self.SAVE_COMMENT_BUTTON)
        time.sleep(2)
        self.do_click(self.CLOSE_COMMENT_MODAL)

















