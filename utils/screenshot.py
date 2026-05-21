import os
import allure


def take_screenshot(driver, name):

    if not os.path.exists("screenshots"):

        os.makedirs("screenshots")

    screenshot_path = f"screenshots/{name}.png"

    driver.save_screenshot(
        screenshot_path
    )

    allure.attach.file(
        screenshot_path,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )