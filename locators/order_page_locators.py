from selenium.webdriver.common.by import By
class OrderPageLocators:
    logo_scooter = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]") # Логотип Самокат
    logo_yandex = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]") # Логотип Яндекс    
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    lastname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    adress_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
    metro_station = (By.XPATH, ".//li[@class='select-search__row']")
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    further_button = (By.XPATH, "//button[contains(@class,'Button_Button__ra12g Button_Middle__1CSJM')]")    
    when_to_bring_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder')]") 
    rental_period_item = (By.XPATH, "//div[contains(@class,'Dropdown-menu')]/div[1]") 
    color_checkbox = (By.XPATH, "//input[@id='black']")
    comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']")
    success_modal = (By.XPATH, '//div[contains(@class,"Order_ModalHeader_")]')