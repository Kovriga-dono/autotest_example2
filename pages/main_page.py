from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import re
from models.contact import Fields
from models.lib import Filling

#данные контакта (вариант с генерацией)
x = 5
contact = Fields(Filling.letters(5),
                 Filling.letters(10),
                 Filling.categ(),
                 Filling.numbers(8),
                 "June 11, 2001")

#данные контакта
# contact = Fields('John',
#                  'Doe',
#                  'Workers',
#                  '0098231',
#                  'June 11, 2001')

#поля для заполнения
firstname_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[2]/td[2]/input')
lastname_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[3]/td[2]/input')
category_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[4]/td[2]/select')
birthday_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[5]/td[2]/input')
addres_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[6]/td[2]/textarea')

#счетчик контактов
counter_selector = (By.XPATH, '//div[@dir="ltr"]')

#кнопка создания контакта
button_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[7]/td/button[2]')


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList')

    def fill_contact_page(self):
#берем оригинальное значение счетчика
        c = re.search(r'\d+$', self.find(counter_selector).text).group()
#заполняем контактные данные
        self.find(firstname_selector).send_keys(contact.first_name)
        self.find(lastname_selector).send_keys(contact.last_name)
        self.find(category_selector).send_keys(contact.category)
        self.find(birthday_selector).send_keys(contact.birthday)
        self.find(firstname_selector).click()
        self.find(addres_selector).send_keys(contact.address)
        self.find(button_selector).click()
#берём счетчик после создания контакта
        b = re.search(r'\d+$', self.find(counter_selector).text).group()
#сравниваем счетчик до и после создания контакта
        assert int(b) == int(c) + 1
