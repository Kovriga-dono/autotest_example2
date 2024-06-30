from selenium import webdriver
import pytest
from time import sleep


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(20)
    chrome_browser.set_window_size(1080, 720)
    return chrome_browser


@pytest.fixture()
def browser_e():
    edge_browser = webdriver.Edge()
    edge_browser.implicitly_wait(20)
    edge_browser.set_window_size(1080, 720)
    return edge_browser

@pytest.fixture()
def browser_f():
    fire_browser = webdriver.Firefox()
    fire_browser.set_window_size(1080, 720)
    fire_browser.implicitly_wait(20)
    return fire_browser
