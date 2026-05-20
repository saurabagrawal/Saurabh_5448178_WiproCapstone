from pages.kids_page import KidsPage
from pages.filter_page import FilterPage

from utils.logger import get_logger


logger = get_logger()


def test_apply_brand_filter(driver):

    kids_page = KidsPage(driver)

    filter_page = FilterPage(driver)

    # Verify Homepage
    kids_page.verify_homepage()

    logger.info("Homepage Verified")

    # Open Kids Section
    kids_page.click_kids_section()

    logger.info("Kids Section Opened")

    # Search Product
    kids_page.search_product("Kids T-shirt")

    logger.info("Product Search Successful")

    # Apply Brand Filter
    filter_page.apply_brand_filter()

    logger.info("Brand Filter Applied")

    # Apply Gender Filter
    filter_page.apply_gender_filter()

    logger.info("Gender Filter Applied")

    # Apply Color Filter
    filter_page.apply_color_filter()

    logger.info("Color Filter Applied")