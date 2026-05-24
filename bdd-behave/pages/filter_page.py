from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class FilterPage(BasePage):
    BRAND_FILTER = (
        By.XPATH,
        "//input[@value='H&M']/parent::label"
    )

    def apply_brand_filter(self):
        # Scroll to filters
        self.driver.execute_script(
            "window.scrollBy(0, 700);"
        )

        brand = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.element_to_be_clickable(
                self.BRAND_FILTER
            )
        )

        # Scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            brand
        )

        # Click filter
        self.driver.execute_script(
            "arguments[0].click();",
            brand
        )