import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    # choose browser (chrome default)
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: firefox or chrome")
    # choose lang
    parser.addoption('--language', action='store', default=None, help="Say language name to select")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    choosen_language = request.config.getoption("language")

    if browser_name == "chrome":
        # chrome init
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': choosen_language})
        browser = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "firefox":
        # firefox init
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", choosen_language)
        browser = webdriver.Firefox(options=options)
    
    yield browser
    print("\nquit browser..")
    browser.quit()

