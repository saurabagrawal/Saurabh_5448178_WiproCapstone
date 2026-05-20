from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class KidsPage(BasePage):

    KIDS_SECTION = (
        By.XPATH,
        "//a[@data-group='kids']"
    )

    SEARCH_BOX = (
        By.CLASS_NAME,
        "desktop-searchBar"
    )

    FIRST_PRODUCT = (
        By.CSS_SELECTOR,
        "li.product-base"
    )

    PRODUCT_TITLE = (
        By.XPATH,
        "//h1"
    )

    NO_RESULTS = (
        By.CLASS_NAME,
        "title-title"
    )

    # VERIFY HOMEPAGE

    def verify_homepage(self):

        self.wait_for_title("Myntra")

        assert "Myntra" in self.driver.title

    # CLICK KIDS SECTION

    def click_kids_section(self):

        self.click_element(
            self.KIDS_SECTION
        )

    # VERIFY KIDS PAGE

    def verify_kids_page_opened(self):

        self.wait_for_title("Kids")

        assert "Kids" in self.driver.title

    # SEARCH PRODUCT

    def search_product(self, product):

        self.enter_text(
            self.SEARCH_BOX,
            product
        )

        search_box = self.get_element(
            self.SEARCH_BOX
        )

        search_box.send_keys(Keys.ENTER)

        self.wait.until(
            lambda d: len(
                d.find_elements(
                    *self.FIRST_PRODUCT
                )
            ) > 0
        )

    # OPEN FIRST PRODUCT

    def open_first_product(self):

        self.wait.until(
            lambda d: len(
                d.find_elements(
                    *self.FIRST_PRODUCT
                )
            ) > 0
        )

        first_product = self.driver.find_elements(
            *self.FIRST_PRODUCT
        )[0]

        product_link = first_product.find_element(
            By.TAG_NAME,
            "a"
        )

        product_url = product_link.get_attribute(
            "href"
        )

        self.driver.get(product_url)

    # VERIFY PRODUCT PAGE

    def verify_product_page_opened(self):

        product = self.get_element(
            self.PRODUCT_TITLE
        )

        assert product.is_displayed()

    # VERIFY NO PRODUCTS FOUND

    def verify_no_products_found(self):

        no_result = self.get_element(
            self.NO_RESULTS
        )

        assert no_result.is_displayed()