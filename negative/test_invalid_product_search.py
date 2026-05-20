from pages.kids_page import KidsPage
from utils.logger import get_logger
import time

logger = get_logger()


def test_invalid_product_search(driver):

    kids_page = KidsPage(driver)

    # Verify Homepage
    kids_page.verify_homepage()

    logger.info("Homepage Verified")

    # Open Kids Section
    kids_page.click_kids_section()

    logger.info("Kids Section Opened")

    # Search Invalid Product
    kids_page.search_product("asdkjasdhj")

    logger.info("Invalid Product Searched")

    # Verify No Products Found
    kids_page.verify_no_products_found()
    time.sleep(10)

    logger.info("No Products Found Verification Passed")