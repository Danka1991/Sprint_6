import allure 
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import test_data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import main_url

class TestOrderForm:
    
    @allure.title('Проверка раздела "Форма заказа')
    @allure.description('Проверка флоу позитивного сценария с двумя наборами данных. Проверка двух точек входа в сценарий: кнопка «Заказать» вверху страницы и внизу. Проверка перехода в Дзена через клик по лого Яндекса и переход на главную если нажать на логотип «Самоката»')
    
    @pytest.mark.parametrize("button,test_data", [
        (MainPageLocators.order_button_up, test_data[0]),
        (MainPageLocators.order_button_down, test_data[1])
    ])
    def test_order_form_through_buttons(self, driver, button, test_data):
        main_page = MainPage(driver)
        main_page.click_order_button(button)

        order_page = OrderPage(driver)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_displaying_of_element(OrderPageLocators.success_modal) == True

    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат"')
    
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button(MainPageLocators.order_button_down)

        order_page = OrderPage(driver)
        order_page.click_on_element(OrderPageLocators.logo_scooter)
        assert main_page.get_current_url() == main_url

    @allure.title('Проверка перехода на страницу "Дзена" при клике на лого "Яндекс"')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_element(OrderPageLocators.logo_yandex)
        main_page.switch_to_next_tab()
        assert main_page.page_url_contains('dzen.ru') == True