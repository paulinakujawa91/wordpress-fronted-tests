import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driverpath = r'C:\Users\Tomek_2\Desktop\kursy_udemy\SELENIUM\chromedriver.exe'

@pytest.fixture()
def setup(request):
    opts = Options()
    opts.add_argument("user-agent=whatever you want")
    driver = webdriver.Chrome(driverpath, chrome_options=opts)
    driver.implicitly_wait(1000)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()