from pages.kids_page import KidsPage

from utils.logger import get_logger
from utils.screenshot import take_screenshot

import time


logger = get_logger()


def test_invalid_product_search(driver):

    kids_page = KidsPage(driver)

    # Verify Homepage
    kids_page.verify_homepage()

    logger.info("Homepage Verified")

    take_screenshot(
        driver,
        "Homepage_Verified"
    )

    # Open Kids Section
    kids_page.click_kids_section()

    logger.info("Kids Section Opened")

    take_screenshot(
        driver,
        "Kids_Section_Opened"
    )

    # Search Invalid Product
    kids_page.search_product("asdkjasdhj")

    logger.info("Invalid Product Searched")

    take_screenshot(
        driver,
        "Invalid_Product_Search"
    )

    # Verify No Products Found
    kids_page.verify_no_products_found()

    logger.info("No Products Found Verification Passed")

    take_screenshot(
        driver,
        "No_Products_Found"
    )

    time.sleep(10)