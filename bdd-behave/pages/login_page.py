from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class LoginPage(BasePage):

    PROFILE_BUTTON = (
        By.CLASS_NAME,
        "desktop-linkButton"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'login / Signup')]"
    )

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@type='tel']"
    )

    CONSENT_CHECKBOX = (
        By.CLASS_NAME,
        "consentCheckbox"
    )

    CONTINUE_BUTTON = (
        By.CLASS_NAME,
        "submitBottomOption"
    )

    DISABLED_CONTINUE = (
        By.CLASS_NAME,
        "disabledSubmitBottomOption"
    )

    OTP_TEXT = (
        By.XPATH,
        "//div[contains(text(),'OTP')]"
    )

    # OPEN LOGIN

    def open_login(self):
        profile = self.wait.until(
            lambda d: d.find_element(
                *self.PROFILE_BUTTON
            )
        )

        ActionChains(self.driver) \
            .move_to_element(profile) \
            .perform()

        login_button = self.wait.until(
            lambda d: d.find_element(
                *self.LOGIN_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_button
        )

        print("Login Popup Opened")
    # ENTER MOBILE NUMBER

    # ENTER MOBILE NUMBER

    def enter_mobile_number(self, number):
        mobile = self.wait.until(
            lambda d: d.find_element(
                *self.MOBILE_INPUT
            )
        )

        mobile.click()

        mobile.clear()

        for digit in str(number):
            mobile.send_keys(digit)

        print("Mobile Number Entered")
    # CLICK CONSENT CHECKBOX

    # CLICK CONSENT CHECKBOX

    def click_consent_checkbox(self):
        self.wait.until(
            lambda d: len(
                d.find_elements(
                    *self.CONSENT_CHECKBOX
                )
            ) > 0
        )

        checkbox = self.driver.find_elements(
            *self.CONSENT_CHECKBOX
        )[0]

        self.driver.execute_script(
            "arguments[0].click();",
            checkbox
        )

        print("Consent Checkbox Clicked")

    # CLICK CONTINUE BUTTON

    # CLICK CONTINUE BUTTON

    def click_continue(self):
        self.wait.until(
            lambda d: len(
                d.find_elements(
                    *self.CONTINUE_BUTTON
                )
            ) > 0
        )

        continue_button = self.driver.find_elements(
            *self.CONTINUE_BUTTON
        )[0]

        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        print("Continue Button Clicked")

    # VERIFY CONTINUE DISABLED

    def verify_continue_disabled(self):

        button = self.get_element(
            self.DISABLED_CONTINUE
        )

        assert button.is_displayed()

        print("Continue Button Disabled Verified")

    # VERIFY OTP PAGE

    def verify_otp_page(self):

        otp = self.get_element(
            self.OTP_TEXT
        )

        assert otp.is_displayed()

        print("OTP Page Verified")