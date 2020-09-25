from Pages.BoardsPage import BoardsPage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from config.config import TestData
import allure


@allure.severity(allure.severity_level.CRITICAL)
class Test_Boards(BaseTest):

    def test_do_stuff(self):
        try:
            self.loginpage = LoginPage(self.driver)
            self.boardspage = BoardsPage(self.driver)
            self.loginpage.do_valid_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)
            self.boardspage.search_board(TestData.BOARD_NAME)
            self.boardspage.create_Not_Started()
            self.boardspage.create_In_Progress()
            self.boardspage.create_QA()
            self.boardspage.create_Done()
            self.boardspage.add_Cards_in_NotStarted()
            self.boardspage.move_Card2_to_InProgress()
            self.boardspage.move_Card3_to_QA()
            self.boardspage.move_Card2_to_QA()
            self.boardspage.assign_Card1_to_CurrentUser(TestData.NAME)

        except Exception as e:
            print("Exception occurred ", e)

