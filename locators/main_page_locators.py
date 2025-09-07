from selenium.webdriver.common.by import By

class MainPageLocators:
    faq_section = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]") # Выпадающий список "Вопросы о важном"
    order_button_down = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM")]')  # Кнопка "Заказать" внизу страницы
    order_button_up = (By.XPATH, '//button[contains(@class,"Button_Button__ra12g")]') # Кнопка "Заказать" вверху страницы
    visible_accordion_panel = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")

    def get_faq_questions_item(text):
        return (By.XPATH, f"//div[contains(@class, 'accordion__button') and text()='{text}']")
    
   