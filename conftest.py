from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(20)
    chrome_browser.set_window_size(1080, 720)
    return chrome_browser
