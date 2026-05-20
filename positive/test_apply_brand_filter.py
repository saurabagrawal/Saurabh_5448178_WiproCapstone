from pages.kids_page import KidsPage
from utils.logger import get_logger


logger = get_logger()


def test_apply_brand_filter(driver):

    kids_page = KidsPage(driver)

    kids_page.verify_homepage()

    kids_page.click_kids_section()

    kids_page.search_product("Kids T-shirt")

    logger.info("Product Search Successful")

    kids_page.apply_brand_filter()

    logger.info("Brand Filter Applied Successfully")