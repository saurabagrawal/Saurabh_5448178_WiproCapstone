from pages.kids_page import KidsPage
from utils.logger import get_logger


logger = get_logger()


def test_search_product(driver):

    kids_page = KidsPage(driver)

    kids_page.verify_homepage()

    logger.info("Homepage Verified")

    kids_page.click_kids_section()

    logger.info("Kids Section Clicked")

    kids_page.search_product("Kids T-shirt")

    logger.info("Product Search Successful")