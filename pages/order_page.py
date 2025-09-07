from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure 

class OrderPage(BasePage):
    
    @allure.step('Заполнение первой части формы + кнопка "Далее"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.name_input)
        self.click_on_element(OrderPageLocators.name_input)
        self.send_keys_to_input(OrderPageLocators.name_input, test_data[0])
        self.click_on_element(OrderPageLocators.lastname_input)
        self.send_keys_to_input(OrderPageLocators.lastname_input, test_data[1])
        self.click_on_element(OrderPageLocators.adress_input)
        self.send_keys_to_input(OrderPageLocators.adress_input, test_data[2])
        self.click_on_element(OrderPageLocators.metro_station_input)
        self.send_keys_to_input(OrderPageLocators.metro_station_input, test_data[3])
        self.click_on_element(OrderPageLocators.metro_station)              
        self.click_on_element(OrderPageLocators.phone_input)
        self.send_keys_to_input(OrderPageLocators.phone_input, test_data[4])
        self.click_on_element(OrderPageLocators.further_button)

    @allure.step('Заполнение второй части формы + кнопка "Далее"')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.when_to_bring_input)
        self.click_on_element(OrderPageLocators.when_to_bring_input)
        self.send_keys_to_input(OrderPageLocators.when_to_bring_input, test_data[5])
        self.click_on_element(OrderPageLocators.color_checkbox)
        self.click_on_element(OrderPageLocators.rental_period)
        self.click_on_element(OrderPageLocators.rental_period_item)
        self.click_on_element(OrderPageLocators.comment_input)
        self.send_keys_to_input(OrderPageLocators.comment_input, test_data[8])
        self.wait_visibility_of_element(OrderPageLocators.order_button)
        self.click_on_element(OrderPageLocators.order_button)