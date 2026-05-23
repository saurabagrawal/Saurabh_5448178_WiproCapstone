import pytest
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from pages.cart_page import CartPage
from pages.kids_page import KidsPage
from pages.login_page import LoginPage

from utils.logger import get_logger
from utils.config_reader import ConfigReader
from utils.csv_reader import get_test_data
from utils.screenshot import take_screenshot


logger = get_logger()

config = ConfigReader()


@pytest.mark.parametrize(
    "product,size,quantity,donation,pincode,expected_title",
    get_test_data("test_data/products.csv")
)

@allure.feature("Myntra Kids E2E")
@allure.story("Search Product And Complete Cart Flow")
def test_myntra_kids_e2e(
    driver,
    product,
    size,
    quantity,
    donation,
    pincode,
    expected_title
):

    wait = WebDriverWait(driver, 20)

    kids_page = KidsPage(driver)
    cart_page = CartPage(driver)
    login_page = LoginPage(driver)

    logger.info("******** Test Started ********")

    # Verify Homepage
    kids_page.verify_homepage()

    logger.info("Homepage Verified Successfully")

    take_screenshot(driver, "Homepage")

    # Open Kids Section
    kids_page.click_kids_section()

    logger.info("Kids Section Opened Successfully")

    take_screenshot(driver, "Kids_Section")

    # Verify Kids Page
    kids_page.verify_kids_page_opened()

    logger.info("Kids Page Verified")

    # Search Product
    kids_page.search_product(product)

    logger.info(f"Search performed for: {product}")

    take_screenshot(driver, "Product_Search")


    # Open First Product
    kids_page.open_first_product()

    logger.info("First Product Opened")

    # Verify Product Page
    kids_page.verify_product_page_opened()

    logger.info("Product Page Verified")

    take_screenshot(driver, "Product_Page")

    # Product Title Assertion
    actual_title = driver.title.lower().replace("-", " ")

    expected = expected_title.lower().replace("-", " ")

    assert expected in actual_title

    logger.info("Expected Product Title Verified")
    # Select Size
    cart_page.select_size()

    logger.info(f"Product Size Selected: {size}")

    # Add To Bag
    cart_page.add_to_bag()

    logger.info("Product Added To Bag")

    # Verify Product Added
    cart_page.verify_product_added()

    logger.info("Product Successfully Added To Bag")

    take_screenshot(driver, "Added_To_Bag")

    # Open Shopping Bag
    cart_page.open_bag()

    logger.info("Shopping Bag Opened")

    # Verify Cart Page
    cart_page.verify_cart_page()

    logger.info("Cart Page Verified Successfully")

    take_screenshot(driver, "Cart_Page")

    # Open Quantity Dropdown
    logger.info("Opening quantity dropdown")

    qty = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'itemComponents-base-quantity')]")
        )
    )

    driver.execute_script("arguments[0].click();", qty)

    # Change Quantity
    logger.info(f"Changing quantity to {quantity}")

    qty_option = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"(//div[contains(@class,'dialogs-base-item')])[{quantity}]"
            )
        )
    )

    try:
        qty_option.click()

    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", qty_option)

    # Select Donation
    logger.info(f"Selecting donation ₹{donation}")

    donate = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[contains(text(),'₹{donation}')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", donate)

    # Place Order
    logger.info("Clicking Place Order")

    place = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'PLACE ORDER')]")
        )
    )

    driver.execute_script("arguments[0].click();", place)

    # Login Redirect Validation
    logger.info("Waiting for login redirect")

    wait.until(
        lambda d: "login" in d.current_url.lower()
    )

    logger.info(f"Redirected URL: {driver.current_url}")

    # Enter Mobile Number
    login_page.enter_mobile_number("9152358202")

    logger.info("Valid Mobile Number Entered")

    take_screenshot(driver, "Valid_Mobile_Number_Entered")

    # Click Consent Checkbox
    login_page.click_consent_checkbox()

    logger.info("Consent Checkbox Clicked")

    take_screenshot(driver, "Consent_Checkbox_Clicked")

    # Click Continue Button
    login_page.click_continue()

    logger.info("Continue Button Clicked")

    take_screenshot(driver, "Continue_Button_Clicked")

    # OTP Assertion
    assert "otp" in driver.page_source.lower()

    logger.info("OTP Page Assertion Passed")

    # Final Allure Screenshot
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Final_Result",
        attachment_type=allure.attachment_type.PNG
    )

    logger.info("******** E2E Test Passed Successfully ********")