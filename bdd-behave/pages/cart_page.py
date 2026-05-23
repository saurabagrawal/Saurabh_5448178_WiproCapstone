from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class CartPage(BasePage):

    SIZE = (
        By.CLASS_NAME,
        "size-buttons-size-button"
    )

    ADD_TO_BAG = (
        By.XPATH,
        "//div[contains(text(),'ADD TO BAG')]"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "desktop-badge"
    )
    BAG = (
        By.XPATH,
        "//a[contains(@href,'checkout/cart')]"
    )

    CART_PRODUCT = (
        By.CLASS_NAME,
        "itemContainer-base-brand"
    )

    # OPEN BAG

    def open_bag(self):
        bag = self.get_element(
            self.BAG
        )

        self.driver.execute_script(
            "arguments[0].click();",
            bag
        )

        print("Shopping Bag Opened")

    # VERIFY CART PAGE

    def verify_cart_page(self):
        cart_product = self.get_element(
            self.CART_PRODUCT
        )

        assert cart_product.is_displayed()

        print("Cart Page Verified")

    def select_size(self):

        self.click_element(
            self.SIZE
        )

    def add_to_bag(self):

        add_button = self.wait.until(
            lambda d: d.find_element(
                *self.ADD_TO_BAG
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_button
        )

    def verify_product_added(self):

        self.wait.until(
            lambda d: len(
                d.find_elements(
                    *self.CART_BADGE
                )
            ) > 0

        )