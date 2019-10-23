import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.basic_page import BasePage


class SearchResultPage(BasePage):
    BUTTON_FOLLOW = (By.XPATH, "//button[@type='button']")

    def get_button_text(self):
        return self.get_text(self.BUTTON_FOLLOW, "Подписаться")