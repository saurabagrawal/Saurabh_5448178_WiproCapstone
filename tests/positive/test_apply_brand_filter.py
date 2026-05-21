from pages.kids_page import KidsPage
from pages.filter_page import FilterPage

from utils.logger import get_logger
from utils.screenshot import take_screenshot


logger = get_logger()


def test_apply_brand_filter(driver):

    kids_page = KidsPage(driver)

    filter_page = FilterPage(driver)

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

    # Apply Brand Filter
    filter_page.apply_brand_filter()

    logger.info("Brand Filter Applied")

    take_screenshot(
        driver,
        "Brand_Filter_Applied"
    )

    # Apply Gender Filter
    filter_page.apply_gender_filter()

    logger.info("Gender Filter Applied")

    take_screenshot(
        driver,
        "Gender_Filter_Applied"
    )

    # Apply Color Filter
    filter_page.apply_color_filter()

    logger.info("Color Filter Applied")

    take_screenshot(
        driver,
        "Color_Filter_Applied"
    )