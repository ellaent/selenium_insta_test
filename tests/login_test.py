import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_result import SearchResultPage

driver = webdriver.Chrome("F:/Python course/chromedriver.exe")
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(60)  # for me to have time to enter the code for authentication

login_page = LoginPage(driver)

login_page.enter_username("ella_ent")
login_page.enter_password("Entina190901")
login_page.login()

main_page = MainPage(driver)
main_page.click_not_now_button()
main_page.type_in_search_field("summer")
main_page.click_result_with_text("#summer")

search_page = SearchResultPage(driver)

if search_page.get_button_text():
    print("it's here:)")

driver.quit()