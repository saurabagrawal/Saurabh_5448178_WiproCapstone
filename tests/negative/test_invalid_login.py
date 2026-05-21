from pages.login_page import LoginPage

from utils.logger import get_logger
from utils.screenshot import take_screenshot


logger = get_logger()


def test_invalid_login(driver):

    login_page = LoginPage(driver)

    # Open Login Popup
    login_page.open_login()

    logger.info("Login Popup Opened")

    take_screenshot(
        driver,
        "Invalid_Login_Popup"
    )

    # Enter Invalid Mobile Number
    login_page.enter_mobile_number("12345")

    logger.info("Invalid Mobile Number Entered")

    take_screenshot(
        driver,
        "Invalid_Mobile_Number_Entered"
    )

    # Click Consent Checkbox
    login_page.click_consent_checkbox()

    logger.info("Consent Checkbox Clicked")

    take_screenshot(
        driver,
        "Consent_Checkbox_Clicked"
    )

    # Click Continue Button
    login_page.click_continue()

    logger.info("Continue Button Clicked")

    take_screenshot(
        driver,
        "Invalid_Login_Continue_Clicked"
    )