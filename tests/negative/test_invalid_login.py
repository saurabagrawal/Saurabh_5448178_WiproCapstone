from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()

def test_invalid_login(driver):

    login_page = LoginPage(driver)

    # Open Login Popup
    login_page.open_login()

    logger.info("Login Popup Opened")

    # Enter Invalid Mobile Number
    login_page.enter_mobile_number("12345")

    logger.info("Invalid Mobile Number Entered")

    # Click Consent Checkbox
    login_page.click_consent_checkbox()

    logger.info("Consent Checkbox Clicked")

    # Click Continue Button
    login_page.click_continue()

    logger.info("Continue Button Clicked")