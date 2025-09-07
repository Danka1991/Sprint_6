from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import BasePage
from locators import Locators

chrome_binary = r'd:\chrome-win64\chrome.exe'

options = Options()
options.binary_location = chrome_binary
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = None
driver = webdriver.Chrome(options=options)
class FaqPage(BasePage):
    question_locator = (By.XPATH, "//div[text()='{}']/../..")???
    answer_locator = (By.XPATH, "//div[text()='{}']/../../following-sibling::div")????
    
    def get_question_element(self, question_text):
        return self.driver.find_element(*self.question_locator)
    
    def get_answer_text(self, question_text):
        return self.get_text(self.answer_locator)
    
    def click_question(self, question_text):????
        self.click(self.question_locator)