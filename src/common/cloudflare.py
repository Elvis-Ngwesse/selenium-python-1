from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass


class CloudFlarePage:
    __login_code_locator = "//*[text()='Get a login code emailed to you']"
    __email_locator = "input[type='email']"
    __send_me_a_code_locator = "button[type='submit']"
    __enter_code_locator = "input[name='code']"
    __sign_in_locator = "button[type='submit']"
    __page_name = 'CloudFlarePage'

    def __init__(self):
        BaseClass.is_page_loaded(By.XPATH, self.__login_code_locator, self.__page_name)

    def enter_user_email(self, email: str):
        BaseClass.element_click(By.CSS_SELECTOR, self.__email_locator)
        BaseClass.set_text(By.CSS_SELECTOR, self.__email_locator, email)

    def click_send_me_a_code_button(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__send_me_a_code_locator)

    def enter_code(self, code: str):
        BaseClass.element_click(By.CSS_SELECTOR, self.__enter_code_locator)
        BaseClass.set_text(By.CSS_SELECTOR, self.__enter_code_locator, code)

    def click_sign_button(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__sign_in_locator)