from pages.kids_page import KidsPage

from utils.logger import get_logger
from utils.screenshot import take_screenshot


logger = get_logger()


def test_open_product_details(driver):

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

    # Search Product
    kids_page.search_product("Kids T-shirt")

    logger.info("Product Search Successful")

    take_screenshot(
        driver,
        "Product_Search_Successful"
    )

    # Open Product
    kids_page.open_first_product()

    logger.info("First Product Opened")

    take_screenshot(
        driver,
        "First_Product_Opened"
    )

    # Verify Product Page
    kids_page.verify_product_page_opened()

    logger.info("Product Details Verified")

    take_screenshot(
        driver,
        "Product_Details_Verified"
    )