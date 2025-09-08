from locators.main_page_locators import MainPageLocators
from pages.yandex_layout_page import YandexPage

import allure 

class MainPage(YandexPage):

    @allure.step('Ожидание загрузки отображения заголовка главной страницы')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Получение ответа на вопрос в списке "Вопросы о важном"')
    def get_displayed_text_from_faq_answer(self):
        return self.get_text_on_element(MainPageLocators.visible_accordion_panel)

    @allure.step('Нажать на верхнюю кнопку "Заказать"')
    def click_order_button_up(self):
        self.scroll_to_element(MainPageLocators.order_button_up)
        self.driver.find_element(*MainPageLocators.order_button_up).click()

    @allure.step('Нажать на нижнюю кнопку "Заказать"')
    def click_order_button_down(self):
        self.scroll_to_element(MainPageLocators.order_button_down)
        self.driver.find_element(*MainPageLocators.order_button_down).click()

    @allure.step('Нажимаеми на вопрос в faq секции')
    def faq_open_question(self, question_text):
        self.wait_visibility_of_element(MainPageLocators.get_faq_questions_item_locator(question_text)).click() 