import pytest

from utils.driver_setup import get_driver
from utils.config_reader import ConfigReader
from utils.screenshot import take_screenshot


config = ConfigReader()


@pytest.fixture
def driver(request):

    driver = get_driver()

    driver.get(config.get("BASE_URL"))

    yield driver

    # Screenshot on failure

    if request.node.rep_call.failed:

        take_screenshot(
            driver,
            request.node.name
        )

    driver.quit()


@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)