from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure 

class MainPage(BasePage):

    @allure.step('Ожидание загрузки отображения заголовка главной страницы')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Получение ответа на вопрос в списке "Вопросы о важном"')
    def get_displayed_text_from_faq_answer(self, data):
        return self.get_text_on_element(data)

    @allure.step('Нажать на верхнюю кнопку "Заказать"')
    def click_order_button(self, button):
        self.scroll_to_element(button)
        self.driver.find_element(*button).click()