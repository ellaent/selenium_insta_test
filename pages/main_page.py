from pages.basic_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    BUTTON_NOT_NOW = (By.XPATH, "//button[text() = 'Не сейчас']")
    FIELD_SEARCH = (By.XPATH, "//input[@placeholder = 'Поиск']")

    def click_not_now_button(self):
        self.click_on(self.BUTTON_NOT_NOW)

    def type_in_search_field(self, text):
        self.type_in(self.FIELD_SEARCH, text)

    def click_result_with_text(self, text):
        result = (By.XPATH, "//span[text()='{}']".format(text))
        self.click_on(result)