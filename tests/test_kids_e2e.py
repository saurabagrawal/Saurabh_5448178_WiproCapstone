import pytest

from pages.kids_page import KidsPage
from utils.logger import get_logger
from utils.config_reader import ConfigReader
from utils.csv_reader import get_test_data

logger = get_logger()

config = ConfigReader()


@pytest.mark.parametrize(
    "product",
    get_test_data("test_data/products.csv")
)

def test_myntra_kids_e2e(driver, product):

    kids_page = KidsPage(driver)

    kids_page.verify_homepage()

    logger.info("Homepage Verified Successfully")

    kids_page.click_kids_section()

    logger.info("Kids Section Opened Successfully")

    kids_page.verify_kids_page_opened()

    kids_page.search_product(product)

    logger.info(f"Search performed for: {product}")

    kids_page.apply_brand_filter()

    logger.info("Brand Filter Applied")

    kids_page.open_first_product()

    logger.info("First Product Opened")

    kids_page.switch_to_product_window()

    logger.info("Switched To Product Window")

    kids_page.verify_product_page_opened()

    logger.info("Product Page Verified")

    kids_page.select_size()

    logger.info("Product Size Selected")

    kids_page.add_to_bag()

    logger.info("Product Added To Bag")

    kids_page.verify_product_added()

    logger.info("Product Successfully Added To Bag")

    kids_page.open_bag()

    logger.info("Shopping Bag Opened")

    kids_page.verify_cart_page()

    logger.info("Cart Page Verified Successfully")