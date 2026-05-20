import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utils.logger import get_logger


logger = get_logger()


@pytest.fixture()

def driver():

    logger.info("Launching Chrome Browser")

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(
        service=service
    )

    driver.maximize_window()

    driver.get(
        "https://www.myntra.com"
    )

    yield driver

    logger.info("Closing Browser")

    driver.quit()