import allure 
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import test_data

from curl import main_url

class TestOrderForm:
    
    @allure.title('Проверка раздела "Форма заказа')
    @allure.description('Проверка флоу позитивного сценария с двумя наборами данных. Проверка двух точек входа в сценарий: кнопка «Заказать» вверху страницы и внизу. Проверка перехода в Дзена через клик по лого Яндекса и переход на главную если нажать на логотип «Самоката»')
    
    @pytest.mark.parametrize("click_btn_method,test_data", [
        ("click_order_button_up", test_data[0]),
        ("click_order_button_down", test_data[1])
    ])
    def test_order_form_through_buttons(self, driver, click_btn_method, test_data):
        main_page = MainPage(driver)
        method = getattr(main_page, click_btn_method)
        method()
        order_page = OrderPage(driver)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_displaying_of_success_modal() == True

    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат"')
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_down()

        order_page = OrderPage(driver)
        order_page.click_on_logo_scooter()
        assert main_page.get_current_url() == main_url

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_logo_yandex()
        main_page.switch_to_next_tab()
        assert main_page.page_url_contains('dzen.ru') == True