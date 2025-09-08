from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure 

class YandexPage(BasePage):
    
    @allure.step('Нажимаем на лого "Яндекс"')
    def click_on_logo_yandex(self):
        return self.click_on_element(OrderPageLocators.logo_yandex)
    
    @allure.step('Нажимаем на лого "Самокат"')
    def click_on_logo_scooter(self):
        return self.click_on_element(OrderPageLocators.logo_scooter)