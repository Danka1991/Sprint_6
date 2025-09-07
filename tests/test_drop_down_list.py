import allure 
import pytest
from pages.main_page import MainPage
from data import questions_answers

class TestMainPage:
    @allure.title('Проверка раздела "Вопросы о важном')
    @allure.description('Проверка появления ответов при нажатии на вопросы')

    @pytest.mark.parametrize("question_text, answer_text", questions_answers)
    def test_faq_question_expansion(self, driver, question_text, answer_text):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.faq_open_question(question_text)
        actual_answer = main_page.get_displayed_text_from_faq_answer()
        assert actual_answer == answer_text

