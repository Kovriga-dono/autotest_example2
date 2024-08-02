import pages.main_page
import pages.base_page
from conftest import browser
import allure
import os
os = os.name

if os == 'mac':

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

# запускает тест для браузера Safari
    @allure.feature('autotest example')
    @allure.story('filling Safari')
    def test_fill_contact_s(browser_s):
        with allure.step('open browser Safari'):
            main_page = pages.main_page.MainPage(browser_s)
        with allure.step('open page'):
            main_page.open()
        with allure.step('filling data'):
            main_pagef = pages.main_page.MainPage(browser_s)
            main_pagef.fill_contact_page()
        with allure.step('close browser'):
            browser_s.quit()
