import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose your language: ru, fr, en")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    browser = None
    chrome_options = Options()

    if browser_language == "ru":
        print("\nstart ru language browser for test..")
        chrome_options.add_experimental_option(
            "prefs",
            {"intl.accept_languages": "ru, ru-RU"}
        )
    elif browser_language == "fr":
        print("\nstart en language browser for test..")
        chrome_options.add_experimental_option(
            "prefs",
            {"intl.accept_languages": "fr, fr-FR"}
        )
    elif browser_language == "en":
        print("\nstart en language browser for test..")
        chrome_options.add_experimental_option(
            "prefs",
            {"intl.accept_languages": "en, en-US"}
        )
    else:
        raise pytest.UsageError("--browser_language should be ru, en or fr")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()