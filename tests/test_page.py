import pages.main_page
import pages.base_page
from conftest import browser


# запускает тест для браузера Chome
def test_fill_contact(browser):
    # открываем браузер
    main_page = pages.main_page.MainPage(browser)
    # переходим на тестируемую страницу
    main_page.open()
    # заполняем данные контакта; создаем контакт; проверяем счетчик
    main_page.fill_contact_page()
    browser.quit()


# запускает тест для браузера EDGE
def test_fill_contact_e(browser_e):
    main_page = pages.main_page.MainPageE(browser_e)
    main_page.open()
    main_page.fill_contact_page_e()
    browser_e.quit()


# запускает тест для браузера FireFox
def test_fill_contact_f(browser_f):
    main_page = pages.main_page.MainPageF(browser_f)
    main_page.open()
    main_page.fill_contact_page_f()
    browser_f.quit()
