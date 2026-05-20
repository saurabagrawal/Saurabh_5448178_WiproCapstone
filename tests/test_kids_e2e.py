import pytest
from pages.cart_page import CartPage
from pages.kids_page import KidsPage
from utils.logger import get_logger
from utils.config_reader import ConfigReader

logger = get_logger()

config = ConfigReader()

# from utils.csv_reader import get_test_data

# @pytest.mark.parametrize(
#     "product",
#     get_test_data("test_data/products.csv")
# )
#
# from utils.json_reader import get_json_data
#
#
# @pytest.mark.parametrize(
#     "product",
#     get_json_data(
#         "test_data/product.json"
#     )
# )

from utils.excel_reader import get_excel_data
@pytest.mark.parametrize(
    "product",
    get_excel_data(
        "test_data/products.xlsx"
    )
)

def test_myntra_kids_e2e(driver, product):

    kids_page = KidsPage(driver)

    cart_page = CartPage(driver)

    # Verify Homepage
    kids_page.verify_homepage()

    logger.info("Homepage Verified Successfully")

    # Open Kids Section
    kids_page.click_kids_section()

    logger.info("Kids Section Opened Successfully")

    # Verify Kids Page
    kids_page.verify_kids_page_opened()

    logger.info("Kids Page Verified")

    # Search Product
    kids_page.search_product(product)

    logger.info(f"Search performed for: {product}")

    # Open Product
    kids_page.open_first_product()

    logger.info("First Product Opened")

    # Verify Product Page
    kids_page.verify_product_page_opened()

    logger.info("Product Page Verified")

    # Select Size
    cart_page.select_size()

    logger.info("Product Size Selected")

    # Add To Bag
    cart_page.add_to_bag()

    logger.info("Product Added To Bag")

    # Verify Product Added
    cart_page.verify_product_added()

    logger.info("Product Successfully Added To Bag")

    cart_page.open_bag()

    logger.info("Shopping Bag Opened")

    cart_page.verify_cart_page()

    logger.info("Cart Page Verified Successfully")