from pages.kids_page import KidsPage
from utils.logger import get_logger


logger = get_logger()


def test_open_product_details(driver):

    kids_page = KidsPage(driver)

    kids_page.verify_homepage()

    kids_page.click_kids_section()

    kids_page.search_product("Kids T-shirt")

    logger.info("Product Search Successful")

    kids_page.open_first_product()

    logger.info("First Product Opened")

    kids_page.switch_to_product_window()

    logger.info("Switched To Product Window")

    kids_page.verify_product_page_opened()

    logger.info("Product Page Verified")