from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class AutomationPractice:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://automationpractice.com/"
        self.dresses_url = "http://automationpractice.com/index.php?id_category=8&controller=category"
        self.login_page_url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        self.my_account_page = "http://automationpractice.com/index.php?controller=my-account"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time). \
            until(EC.presence_of_element_located(locator),
                  message=f"""Can't find element by locator {locator} """)

    # def find_elements(self, locator, time=10):
    #     return WebDriverWait(self.driver, time). \
    #         until(EC.presence_of_all_elements_located(locator),
    #               message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_login_page(self):
        return self.driver.get(self.login_page_url)

    def mouse_over(self, to_element):
        hover = ActionChains(self.driver)
        element = self.find_element(to_element)
        hover.move_to_element(element)
        hover.perform()

    def select_from_dropdown(self, locator, index):
        Select(self.find_element(locator)).select_by_index(index)

    def teardown(self):
        return self.driver.delete_all_cookies()
