import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Edge"
        # default browser is set as chrome,the --browser_name should be same with the --browser_nam in cmd
    )
    parser.addoption(
        "--username", action="store", default="saheli.mondal@fedev.cbnits.com"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(r"C:\Users\Saheli Mondal\Downloads\chromedriver_win32 (2)\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "Firefox":
        print("firefox driver")
        service_obj = Service(r"C:\Users\Saheli Mondal\Downloads\geckodriver-v0.32.0-win-aarch64\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        service_obj = Service(r"C:\Users\Saheli Mondal\Downloads\chromedriver_win32 (2)\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&flowName=GlifWebSignIn&flowEntry"
               "=ServiceLogin")
    driver.maximize_window()
    request.cls.driver = driver


@pytest.fixture(scope="class")
def get_username(request):
    username = request.config.getoption("username")
    print(get_username)
    return username
