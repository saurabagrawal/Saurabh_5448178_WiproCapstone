from behave import given, when, then

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from pages.cart_page import CartPage
from pages.kids_page import KidsPage
from pages.login_page import LoginPage

from utils.screenshot_util import ScreenshotUtil
from utils.setup_logger import LogGen
from utils.config_reader import ConfigReader

logger = LogGen.loggen()



# =====================================================
# COMMON SETUP
# =====================================================

@given("User launches Myntra website in e2e")
def launch_myntra(context):
    context.driver.get(
        ConfigReader.get_base_url()
    )

    context.wait = WebDriverWait(
        context.driver,
        20
    )

    context.kids_page = KidsPage(
        context.driver
    )

    context.cart_page = CartPage(
        context.driver
    )

    context.login_page = LoginPage(
        context.driver
    )

    logger.info(
        "Myntra Website Launched"
    )


# =====================================================
# HOMEPAGE
# =====================================================

@then("User verifies homepage successfully in e2e")
def verify_homepage(context):

    context.kids_page.verify_homepage()

    logger.info(
        "Homepage Verified Successfully"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Homepage"
    )


# =====================================================
# KIDS SECTION
# =====================================================

@when("User opens kids section in e2e")
def open_kids_section(context):

    context.kids_page.click_kids_section()

    logger.info(
        "Kids Section Opened Successfully"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Kids_Section"
    )


@then("User verifies kids page successfully in e2e")
def verify_kids_page(context):

    context.kids_page.verify_kids_page_opened()

    logger.info(
        "Kids Page Verified"
    )


# =====================================================
# SEARCH PRODUCT
# =====================================================

@when('User searches for "{product}" in e2e')
def search_product(context, product):

    context.kids_page.search_product(
        product
    )

    logger.info(
        f"Search performed for: {product}"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Product_Search"
    )


# =====================================================
# PRODUCT PAGE
# =====================================================

@when("User opens first product in e2e")
def open_first_product(context):

    context.kids_page.open_first_product()

    logger.info(
        "First Product Opened"
    )


@then("User verifies product page successfully in e2e")
def verify_product_page(context):

    context.kids_page.verify_product_page_opened()

    logger.info(
        "Product Page Verified"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Product_Page"
    )


# =====================================================
# SIZE
# =====================================================

@when("User selects product size in e2e")
def select_size(context):

    context.cart_page.select_size()

    logger.info(
        "Product Size Selected"
    )


# =====================================================
# ADD TO BAG
# =====================================================

@when("User adds product to bag in e2e")
def add_to_bag(context):

    context.cart_page.add_to_bag()

    logger.info(
        "Product Added To Bag"
    )


@then("User verifies product added successfully in e2e")
def verify_product_added(context):

    context.cart_page.verify_product_added()

    logger.info(
        "Product Successfully Added To Bag"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Added_To_Bag"
    )


# =====================================================
# SHOPPING BAG
# =====================================================

@when("User opens shopping bag in e2e")
def open_bag(context):

    context.cart_page.open_bag()

    logger.info(
        "Shopping Bag Opened"
    )


@then("User verifies cart page successfully in e2e")
def verify_cart_page(context):

    context.cart_page.verify_cart_page()

    logger.info(
        "Cart Page Verified Successfully"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Cart_Page"
    )


# =====================================================
# QUANTITY
# =====================================================

@when('User changes quantity to "{quantity}" in e2e')
def change_quantity(context, quantity):

    logger.info(
        f"Changing quantity to {quantity}"
    )

    qty = context.wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'itemComponents-base-quantity')]"
            )
        )
    )

    context.driver.execute_script(
        "arguments[0].click();",
        qty
    )

    qty_option = context.wait.until(
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

        context.driver.execute_script(
            "arguments[0].click();",
            qty_option
        )


# =====================================================
# DONATION
# =====================================================

@when('User selects donation "{donation}" in e2e')
def select_donation(context, donation):

    logger.info(
        f"Selecting donation ₹{donation}"
    )

    donate = context.wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"//div[contains(text(),'₹{donation}')]"
            )
        )
    )

    context.driver.execute_script(
        "arguments[0].click();",
        donate
    )


# =====================================================
# PLACE ORDER
# =====================================================

@when("User clicks place order in e2e")
def click_place_order(context):

    logger.info(
        "Clicking Place Order"
    )

    place = context.wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'PLACE ORDER')]"
            )
        )
    )

    context.driver.execute_script(
        "arguments[0].click();",
        place
    )


# =====================================================
# LOGIN REDIRECT
# =====================================================

@then("User should be redirected to login page in e2e")
def verify_login_redirect(context):

    context.wait.until(
        lambda d: "login" in d.current_url.lower()
    )

    logger.info(
        f"Redirected URL: {context.driver.current_url}"
    )


# =====================================================
# LOGIN
# =====================================================

@when('User enters mobile number "{number}" in e2e')
def enter_mobile(context, number):

    context.login_page.enter_mobile_number(
        number
    )

    logger.info(
        "Valid Mobile Number Entered"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Valid_Mobile_Number_Entered"
    )


@when("User clicks consent checkbox in e2e")
def click_checkbox(context):

    context.login_page.click_consent_checkbox()

    logger.info(
        "Consent Checkbox Clicked"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Consent_Checkbox_Clicked"
    )


@when("User clicks continue button in e2e")
def click_continue(context):

    context.login_page.click_continue()

    logger.info(
        "Continue Button Clicked"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Continue_Button_Clicked"
    )


# =====================================================
# OTP
# =====================================================

@then("OTP page should display successfully in e2e")
def verify_otp(context):

    assert "otp" in (
        context.driver.page_source.lower()
    )

    logger.info(
        "OTP Page Assertion Passed"
    )

    allure.attach(
        context.driver.get_screenshot_as_png(),
        name="Final_Result",
        attachment_type=allure.attachment_type.PNG
    )

    logger.info(
        "Complete E2E Test Passed Successfully"
    )