from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ele.text

    def send_keys_enter(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def do_get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def do_drag_and_drop(self, by_locator, source, target):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.click_and_hold(source).pause(5).move_to_element(target).release(target).perform()

    def do_mouse_hover(self, by_locator, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        hover = ActionChains(self.driver)
        hover.move_to_element(element).perform()




