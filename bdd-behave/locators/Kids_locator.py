
from selenium.webdriver.common.by import By


class KidsLocators:

    # ==========================================
    # SEARCH
    # ==========================================

    SEARCH_BOX = (
        By.CLASS_NAME,
        "desktop-searchBar"
    )

    SEARCH_HEADING = (
        By.CLASS_NAME,
        "title-title"
    )

    # ==========================================
    # KIDS MENU
    # ==========================================

    KIDS_MENU = (
        By.XPATH,
        "//a[@data-group='kids']"
    )

    # ==========================================
    # PRODUCTS
    # ==========================================

    PRODUCTS = (
        By.XPATH,
        "//li[contains(@class,'product-base')]//a"
    )

    PDP_TITLE = (
        By.CLASS_NAME,
        "pdp-title"
    )

    # ==========================================
    # SIZE
    # ==========================================

    SIZE = (
        By.XPATH,
        "(//div[contains(@class,'size-buttons-size-button') or contains(@class,'size-buttons-unified-size')])[1]"
    )

    # ==========================================
    # BAG
    # ==========================================

    ADD_TO_BAG = (
        By.XPATH,
        "//div[contains(text(),'ADD TO BAG')]"
    )

    GO_TO_BAG = (
        By.XPATH,
        "//span[contains(text(),'GO TO BAG')]"
    )

    CART_ITEM = (
        By.CLASS_NAME,
        "itemContainer-base-item"
    )

    # ==========================================
    # QUANTITY
    # ==========================================

    QUANTITY_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class,'itemComponents-base-quantity')]"
    )

    QUANTITY_TWO = (
        By.XPATH,
        "(//div[contains(@class,'dialogs-base-item')])[2]"
    )

    # ==========================================
    # DONATION
    # ==========================================

    DONATION = (
        By.XPATH,
        "//div[contains(.,'₹10')]"
    )

    # ==========================================
    # PLACE ORDER
    # ==========================================

    PLACE_ORDER = (
        By.XPATH,
        "//button[contains(.,'PLACE ORDER')]"
    )

    # ==========================================
    # POPUP
    # ==========================================

    POPUP_CLOSE = (
        By.XPATH,
        "//span[contains(@class,'desktop-iconClose')]"
    )
