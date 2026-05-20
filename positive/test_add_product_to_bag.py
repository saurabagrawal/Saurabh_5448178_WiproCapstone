from pages.kids_page import KidsPage
from utils.logger import get_logger


logger = get_logger()


def test_add_product_to_bag(driver):

    kids_page = KidsPage(driver)

    kids_page.verify_homepage()

    kids_page.click_kids_section()

    kids_page.search_product("Kids T-shirt")

    kids_page.apply_brand_filter()

    kids_page.open_first_product()

    kids_page.switch_to_product_window()

    kids_page.verify_product_page_opened()

    kids_page.select_size()

    logger.info("Size Selected")

    kids_page.add_to_bag()

    logger.info("Product Added To Bag")

    kids_page.verify_product_added()

    logger.info("Product Added Verification Passed")