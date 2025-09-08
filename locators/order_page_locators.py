from selenium.webdriver.common.by import By

class OrderPageLocators:
    logo_scooter =(By.XPATH, "//a[contains(@href, 'scooter') or contains(@class, 'LogoScooter')]") # Логотип Самокат   
    logo_yandex = (By.XPATH, "//a[contains(@href, 'yandex') or contains(@class, 'LogoYandex')]") # Логотип Яндекс    
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    lastname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    adress_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    further_button = (By.XPATH, "//button[text()='Далее']")    
    when_to_bring_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period = (By.XPATH, "//div[text()='* Срок аренды']") 
    comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']")
    success_modal = (By.XPATH, '//div[contains(@class,"Order_ModalHeader_")]')

    def get_metro_station_locator(text):
        return (By.XPATH, f"//li[contains(@class, 'select-search__row')]//div[contains(@class, 'Order_Text_') and text()='{text}']")

    def get_rental_period_locator(text):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-menu')]//div[text()='{text}']")
    
    def get_color_checkbox_locator(color):
        return (By.XPATH, f"//input[@id='{color}']")