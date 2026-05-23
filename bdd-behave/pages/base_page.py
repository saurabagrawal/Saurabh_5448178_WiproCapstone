from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 15)

    # CLICK ELEMENT

    def click_element(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # SEND KEYS

    def enter_text(self, locator, text):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)

    # GET ELEMENT

    def get_element(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    # WAIT FOR TITLE

    def wait_for_title(self, text):

        self.wait.until(
            EC.title_contains(text)
        )