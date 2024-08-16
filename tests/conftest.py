import pytest
from selenium import webdriver

from utilities import readConfig

@pytest.fixture
def setup_and_teardown(request):
    browser = readConfig.read_configuration("basic info","browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Specify the right browser")
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = readConfig.read_configuration("basic info","url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()