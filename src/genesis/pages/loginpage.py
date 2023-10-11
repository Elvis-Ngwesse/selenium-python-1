from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass


class LoginPage:
    __welcome_back_locator = "//*[text()='Welcome Back!']"
    __email_locator = "input[type='email']"
    __password_locator = "input[type='password']"
    ___locator = "button[type='submit']"
    __checkbox_locator = "input[type='checkbox']"
    __login_locator = "//*[text()='Log In']"
    __page_name = 'LoginPage'

    def __init__(self):
        BaseClass.is_page_loaded(By.XPATH, self.__welcome_back_locator, self.__page_name)

    def enter_user_email(self, email: str):
        BaseClass.element_click(By.CSS_SELECTOR, self.__email_locator)
        BaseClass.set_text(By.CSS_SELECTOR, self.__email_locator, email)

    def enter_user_password(self, password: str):
        BaseClass.element_click(By.CSS_SELECTOR, self.__password_locator)
        BaseClass.set_text(By.CSS_SELECTOR, self.__password_locator, password)

    def select_remember_me_checkbox(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__checkbox_locator)

    def click_on_login_button(self):
        BaseClass.element_click(By.XPATH, self.__login_locator)