from behave import given, when, then

from pages.kids_page import KidsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.filter_page import FilterPage
import allure
from utils.screenshot_util import ScreenshotUtil
from utils.setup_logger import LogGen
from utils.config_reader import ConfigReader


logger = LogGen.loggen()



# =====================================================
# COMMON SETUP
# =====================================================

@given("User launches Myntra website")
def launch_myntra(context):
    
    context.driver.get(
        ConfigReader.get_base_url()
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

    context.filter_page = FilterPage(
        context.driver
    )

    logger.info(
        "Myntra Website Launched"
    )


# =====================================================
# HOMEPAGE
# =====================================================

@then("User verifies homepage successfully")
def verify_homepage(context):

    context.kids_page.verify_homepage()

    logger.info(
        "Homepage Verified"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Homepage_Verified"
    )


# =====================================================
# KIDS SECTION
# =====================================================

@when("User opens kids section")
def open_kids_section(context):

    context.kids_page.click_kids_section()

    logger.info(
        "Kids Section Opened"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Kids_Section_Opened"
    )


@then("User verifies kids page successfully")
def verify_kids_page(context):

    assert "kids" in (
        context.driver.current_url.lower()
    )

    logger.info(
        "Kids Section Verified"
    )


# =====================================================
# SEARCH PRODUCT
# =====================================================

@when('User searches for "{product}"')
def search_product(context, product):

    context.kids_page.search_product(
        product
    )

    logger.info(
        f"Product Searched: {product}"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Product_Search"
    )


# =====================================================
# INVALID SEARCH
# =====================================================

@then("No products should display")
def verify_no_products(context):

    assert (
        context.kids_page
        .verify_no_products_found()
    )

    logger.info(
        "No Products Found"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "No_Products_Found"
    )


# =====================================================
# BRAND FILTER
# =====================================================

@when("User applies brand filter")
def apply_brand_filter(context):

    context.filter_page.apply_brand_filter()

    logger.info(
        "Brand Filter Applied"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Brand_Filter"
    )


@then("Brand filter should apply successfully")
def verify_brand_filter(context):

    assert "h&m" in (
        context.driver.page_source.lower()
    )

    logger.info(
        "Brand Filter Verified"
    )


# =====================================================
# OPEN PRODUCT
# =====================================================

@when("User opens first product")
def open_first_product(context):

    context.kids_page.open_first_product()

    logger.info(
        "First Product Opened"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "First_Product"
    )


@then("User verifies product page successfully")
def verify_product_page(context):

    assert "buy" in (
        context.driver.current_url.lower()
    )

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

@when("User selects product size")
def select_size(context):

    context.cart_page.select_size()

    logger.info(
        "Size Selected"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Size_Selected"
    )


# =====================================================
# ADD TO BAG
# =====================================================
@when("User adds product to bag")
def add_to_bag(context):

    context.cart_page.add_to_bag()

    logger.info(
        "Product Added To Bag"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Add_To_Bag"
    )


@then("User verifies product added successfully")
def verify_product_added(context):

    assert "bag" in (
        context.driver.page_source.lower()
    )

    logger.info(
        "Product Added Verification Passed"
    )


# =====================================================
# LOGIN
# =====================================================

@when("User opens login popup")
def open_login_popup(context):

    context.login_page.open_login()

    logger.info(
        "Login Popup Opened"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Login_Popup"
    )


@when('User enters mobile number "{number}"')
def enter_mobile(context, number):

    context.login_page.enter_mobile_number(
        number
    )

    logger.info(
        f"Mobile Number Entered: {number}"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Mobile_Number"
    )


@when("User clicks consent checkbox")
def click_checkbox(context):

    context.login_page.click_consent_checkbox()

    logger.info(
        "Consent Checkbox Clicked"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Consent_Checkbox"
    )


@when("User clicks continue button")
def click_continue(context):

    context.login_page.click_continue()

    logger.info(
        "Continue Button Clicked"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Continue_Button"
    )


# =====================================================
# VALID LOGIN
# =====================================================

@then("OTP page should display successfully")
def verify_otp(context):

    assert "otp" in (
        context.driver.page_source.lower()
    )

    logger.info(
        "OTP Page Verified"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "OTP_Page"
    )


# =====================================================
# INVALID LOGIN
# =====================================================

@then("Valid mobile number error should display")
def verify_invalid_mobile(context):

    assert "valid mobile number" in (
        context.driver.page_source.lower()
    )

    logger.info(
        "Invalid Mobile Validation Passed"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "Invalid_Mobile"
    )