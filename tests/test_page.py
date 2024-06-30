from pages.main_page import MainPage
from conftest import browser


def test_fill_contact(browser):
#открываем браузер
    main_page = MainPage(browser)
#переходим на тестируемую страницу
    main_page.open()
#заполняем данные контакта; создаем контакт; проверяем счетчик
    main_page.fill_contact_page()
