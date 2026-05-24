from behave import given, when, then

from pages.kids_page import KidsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.filter_page import FilterPage

from utils.screenshot_util import ScreenshotUtil
from utils.excel_reader import ExcelReader
from utils.logger import LogGen
logger = LogGen.loggen()

urls = load_test_data(
    "urls.json"
)


# =====================================================
# COMMON SETUP
# =====================================================

@given("User launches Myntra website")
def launch_myntra(context):

    context.driver.get(
        urls["base_url"]
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
# HOMEPAGE VALIDATION
# =====================================================

@then("User verifies homepage successfully")
def verify_homepage(context):

    context.kids_page.verify_homepage()

    logger.info(
        "Homepage Verified"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "homepage_verified"
    )

    assert "myntra" in (
        context.driver.title.lower()
    )

    logger.info(
        "Homepage Assertion Passed"
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
        "kids_section_opened"
    )


@then("User verifies kids page successfully")
def verify_kids_page(context):

    assert "kids" in (
        context.driver.current_url.lower()
    )

    logger.info(
        "Kids Section Assertion Passed"
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
        f"Product Search Successful: {product}"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "product_search"
    )


# =====================================================
# INVALID SEARCH VALIDATION
# =====================================================

@then("No products should display")
def verify_no_products(context):

    assert (
        context.kids_page
        .verify_no_products_found()
    )

    logger.info(
        "No Products Found Verification Passed"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "no_products_found"
    )


# =====================================================
# BRAND FILTER
# =====================================================

@when("User applies brand filter")
def apply_brand_filter(context):

    context.filter_page.apply_available_brand_filter()

    logger.info(
        "Brand Filter Applied"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "brand_filter_applied"
    )


@then("Brand filter should apply successfully")
def verify_brand_filter(context):

    assert "filters" in (
        context.driver.page_source.lower()
    )

    logger.info(
        "Brand Filter Assertion Passed"
    )


# =====================================================
# PRODUCT PAGE
# =====================================================

@when("User opens first product")
def open_first_product(context):

    context.kids_page.open_first_product()

    logger.info(
        "First Product Opened"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "first_product_opened"
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
        "product_page_verified"
    )


# =====================================================
# SIZE SELECTION
# =====================================================

@when("User selects product size")
def select_size(context):

    context.cart_page.select_size()

    logger.info(
        "Size Selected"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "size_selected"
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
        "product_added_to_bag"
    )


@then("User verifies product added successfully")
def verify_product_added(context):

    assert "bag" in (
        context.driver.page_source.lower()
    )

    logger.info(
        "Add To Bag Verified"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "add_to_bag_verified"
    )


# =====================================================
# LOGIN POPUP
# =====================================================

@when("User opens login popup")
def open_login_popup(context):

    context.login_page.open_login()

    logger.info(
        "Login Popup Opened"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "login_popup_opened"
    )


# =====================================================
# MOBILE NUMBER
# =====================================================

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
        "mobile_number_entered"
    )


# =====================================================
# CONSENT CHECKBOX
# =====================================================

@when("User clicks consent checkbox")
def click_checkbox(context):

    context.login_page.click_consent_checkbox()

    logger.info(
        "Consent Checkbox Clicked"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "checkbox_clicked"
    )


# =====================================================
# CONTINUE BUTTON
# =====================================================

@when("User clicks continue button")
def click_continue(context):

    context.login_page.click_continue()

    logger.info(
        "Continue Button Clicked"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "continue_clicked"
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
        "OTP Page Assertion Passed"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "otp_page_verified"
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
        "Invalid Login Error Verification Passed"
    )

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "invalid_login_verified"
    )