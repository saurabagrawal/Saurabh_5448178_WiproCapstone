from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class KidsPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

    # LOCATORS

    KIDS_SECTION = (
        By.XPATH,
        "//a[@data-group='kids']"
    )

    SEARCH_BOX = (
        By.CLASS_NAME,
        "desktop-searchBar"
    )

    BRAND_FILTER = (
        By.XPATH,
        "(//label[contains(@class,'common-customCheckbox')])[1]"
    )

    FIRST_PRODUCT = (
        By.CSS_SELECTOR,
        "li.product-base"
    )

    PRODUCT_TITLE = (
        By.XPATH,
        "//h1"
    )

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

    # you have to pin this for e2e
    NO_RESULTS = (
        By.CLASS_NAME,
        "title-title"
    )

    WISHLIST_BUTTON = (
        By.XPATH,
        "//span[contains(text(),'Wishlist')]"
    )

    LOGIN_POPUP = (
        By.XPATH,
        "//input[@placeholder='Mobile Number*']"
    )
    # till here
    # VERIFY HOMEPAGE

    def verify_homepage(self):

        self.wait_for_title("Myntra")

        assert "Myntra" in self.driver.title

        print("Homepage Verified")

    # CLICK KIDS SECTION

    def click_kids_section(self):

        self.click_element(
            self.KIDS_SECTION
        )

    # VERIFY KIDS PAGE

    def verify_kids_page_opened(self):

        self.wait_for_title("Kids")

        assert "Kids" in self.driver.title

        print("Kids Page Verified")

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

    # APPLY BRAND FILTER

    def apply_brand_filter(self):

        brand = self.get_element(
            self.BRAND_FILTER
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            brand
        )

        self.driver.execute_script(
            "arguments[0].click();",
            brand
        )

        print("Brand Filter Applied")

    # OPEN FIRST PRODUCT

    def open_first_product(self):

        self.wait.until(
            lambda d: len(
                d.find_elements(
                    *self.FIRST_PRODUCT
                )
            ) > 0
        )

        products = self.driver.find_elements(
            *self.FIRST_PRODUCT
        )

        first_product = products[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            first_product
        )

        ActionChains(self.driver)\
            .move_to_element(first_product)\
            .click()\
            .perform()

    # SWITCH TO PRODUCT WINDOW

    def switch_to_product_window(self):

        self.wait.until(
            lambda d: len(
                d.window_handles
            ) > 1
        )

        windows = self.driver.window_handles

        self.driver.switch_to.window(
            windows[1]
        )

        print("Switched to Product Window")

    # VERIFY PRODUCT PAGE

    def verify_product_page_opened(self):

        product = self.get_element(
            self.PRODUCT_TITLE
        )

        assert product.is_displayed()

        print("Product Page Verified")

    # SELECT SIZE

    def select_size(self):

        try:

            self.click_element(
                self.SIZE
            )

        except:

            print("Size not available")

    # ADD TO BAG

    def add_to_bag(self):

        self.click_element(
            self.ADD_TO_BAG
        )

    # VERIFY PRODUCT ADDED

    def verify_product_added(self):

        cart = self.get_element(
            self.CART_BADGE
        )

        assert cart.is_displayed()

        print("Product Added Verified")

    # OPEN BAG

    def open_bag(self):

        self.click_element(
            self.BAG
        )

    # VERIFY CART PAGE

    def verify_cart_page(self):

        cart_product = self.get_element(
            self.CART_PRODUCT
        )

        assert cart_product.is_displayed()

        print("Cart Page Verified")

    # VERIFY NO PRODUCTS FOUND

    def verify_no_products_found(self):

        no_result = self.get_element(
            self.NO_RESULTS
        )

        assert no_result.is_displayed()

        print("No Products Found Verified")

    # VERIFY EMPTY CART
    # this also pin for e2e
    # VERIFY SIZE ERROR

    # CLICK WISHLIST

    def click_wishlist(self):

        self.click_element(
            self.WISHLIST_BUTTON
        )

    # VERIFY LOGIN POPUP

    # VERIFY SIZE SECTION DISPLAYED

    def verify_size_section(self):

        size = self.get_element(
            self.SIZE_SECTION
        )

        assert size.is_displayed()

        print("Size Section Verified")