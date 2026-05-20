from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FilterPage(BasePage):

    BRAND_FILTER = (
        By.XPATH,
        "(//label[contains(@class,'common-customCheckbox')])[2]"
    )

    GENDER_FILTER = (
        By.XPATH,
        "//label[contains(.,'Girls')]"
    )

    COLOR_FILTER = (
        By.XPATH,
        "//label[contains(.,'Blue')]"
    )

    FIRST_PRODUCT = (
        By.CSS_SELECTOR,
        "li.product-base"
    )

    def apply_brand_filter(self):

        brand = self.get_element(
            self.BRAND_FILTER
        )

        self.driver.execute_script(
            "arguments[0].click();",
            brand
        )

    def apply_gender_filter(self):

        gender = self.get_element(
            self.GENDER_FILTER
        )

        self.driver.execute_script(
            "arguments[0].click();",
            gender
        )

    def apply_color_filter(self):

        color = self.get_element(
            self.COLOR_FILTER
        )

        self.driver.execute_script(
            "arguments[0].click();",
            color
        )