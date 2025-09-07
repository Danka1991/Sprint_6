import allure 
import pytest
from pages.main_page import MainPage
from data import questions_answers
from locators.main_page_locators import MainPageLocators

class TestMainPage:
    @allure.title('Проверка раздела "Вопросы о важном')
    @allure.description('Проверка появления ответов при нажатии на вопросы')

    @pytest.mark.parametrize("question_text, answer_text", questions_answers)
    def test_faq_question_expansion(self, driver, question_text, answer_text):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_element(MainPageLocators.get_faq_questions_item(question_text)).click()
        main_page.wait_visibility_of_element(MainPageLocators.visible_accordion_panel)
        text_in_visible_panel = main_page.get_displayed_text_from_faq_answer(MainPageLocators.visible_accordion_panel)
        assert text_in_visible_panel == answer_text
