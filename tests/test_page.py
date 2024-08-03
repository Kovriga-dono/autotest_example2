import pages.main_page
import pages.base_page
from conftest import browser
import allure
import os

# тесты для Chrome и FireFox будут запускаться для Winows, MacOS и Linux
# запускает тест для браузера Chome
@allure.feature('autotest example')
@allure.story('filling Chrome')
def test_fill_contact(browser):
    # открываем браузер
    with allure.step('open browser Chrome'):
        main_page = pages.main_page.MainPage(browser)
        # переходим на тестируемую страницу
    with allure.step('open page'):
        main_page.open()
    # заполняем данные контакта; создаем контакт; проверяем счетчик
    with allure.step('filling data'):
        main_pageс = pages.main_page.MainPage(browser)
        main_pageс.fill_contact_page()
    with allure.step('close browser'):
        browser.quit()

# запускает тест для браузера FireFox
@allure.feature('autotest example')
@allure.story('filling FireFox')
def test_fill_contact_f(browser_f):
    with allure.step('open browser FireFox'):
        main_page = pages.main_page.MainPage(browser_f)
    with allure.step('open page'):
        main_page.open()
    with allure.step('filling data'):
        main_pagef = pages.main_page.MainPage(browser_f)
        main_pagef.fill_contact_page()
    with allure.step('close browser'):
        browser_f.quit()

#EDGE тестируем только для Windows
if os.name == 'nt':
    # запускает тест для браузера EDGE
    @allure.feature('autotest example')
    @allure.story('filling Edge')
    def test_fill_contact_e(browser_e):
        with allure.step('open browser Edge'):
            main_page = pages.main_page.MainPage(browser_e)
        with allure.step('open page'):
            main_page.open()
        with allure.step('filling data'):
            main_pagee = pages.main_page.MainPage(browser_e)
            main_pagee.fill_contact_page()
        with allure.step('close browser'):
            browser_e.quit()
#Safari тестируем только в MacOS
elif os.name == 'mac':
    # запускает тест для браузера EDGE
    @allure.feature('autotest example')
    @allure.story('filling Edge')
    def test_fill_contact_m(browser_m):
        with allure.step('open browser Edge'):
            main_page = pages.main_page.MainPage(browser_m)
        with allure.step('open page'):
            main_page.open()
        with allure.step('filling data'):
            main_pagee = pages.main_page.MainPage(browser_m)
            main_pagee.fill_contact_page()
        with allure.step('close browser'):
            browser_m.quit()
