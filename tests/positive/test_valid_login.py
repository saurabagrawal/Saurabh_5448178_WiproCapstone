from pages.login_page import LoginPage

from utils.logger import get_logger
from utils.screenshot import take_screenshot


logger = get_logger()


def test_valid_login(driver):

    login_page = LoginPage(driver)

    # Open Login Popup
    login_page.open_login()

    logger.info("Login Popup Opened")

    take_screenshot(
        driver,
        "Login_Popup_Opened"
    )

    # Enter Valid Mobile Number
    login_page.enter_mobile_number("9152358202")

    logger.info("Valid Mobile Number Entered")

    take_screenshot(
        driver,
        "Valid_Mobile_Number_Entered"
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
        "Continue_Button_Clicked"
    )