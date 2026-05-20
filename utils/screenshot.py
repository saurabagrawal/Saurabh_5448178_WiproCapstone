import os
import allure

from datetime import datetime
from allure_commons.types import AttachmentType


def take_screenshot(driver, test_name):

    folder = "screenshots"

    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"{test_name}_{timestamp}.png"

    path = os.path.join(folder, file_name)

    driver.save_screenshot(path)

    print(f"Screenshot saved: {path}")

    # Attach screenshot to Allure Report
    allure.attach.file(
        path,
        name=test_name,
        attachment_type=AttachmentType.PNG
    )

    return path