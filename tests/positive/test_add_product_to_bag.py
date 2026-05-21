from pages.kids_page import KidsPage
from pages.cart_page import CartPage

from utils.logger import get_logger
from utils.screenshot import take_screenshot


logger = get_logger()


def test_add_product_to_bag(driver):

    kids_page = KidsPage(driver)

    cart_page = CartPage(driver)

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

    logger.info("Product Opened")

    take_screenshot(
        driver,
        "Product_Opened"
    )

    # Verify Product Page
    kids_page.verify_product_page_opened()

    logger.info("Product Page Verified")

    take_screenshot(
        driver,
        "Product_Page_Verified"
    )

    # Select Size
    cart_page.select_size()

    logger.info("Size Selected")

    take_screenshot(
        driver,
        "Product_Size_Selected"
    )

    # Add To Bag
    cart_page.add_to_bag()

    logger.info("Product Added To Bag")

    take_screenshot(
        driver,
        "Product_Added_To_Bag"
    )

    # Verify Product Added
    cart_page.verify_product_added()

    logger.info("Add To Bag Verified")

    take_screenshot(
        driver,
        "Add_To_Bag_Verified"
    )