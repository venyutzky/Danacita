from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest

#To run
## pytest -vs --browser chrome --url https://danacita.co.id/

@pytest.fixture(scope="class")
def setup(request, browser, url):
    
    if browser == "chrome":
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)
    elif browser == "edge":
        option = webdriver.EdgeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver  = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=option)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()
    
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)    
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)    
def url(request):
    return request.config.getoption("--url")