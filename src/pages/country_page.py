from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass


class CountryPage:
    __country_locator = "//*[text()='Choose Country']"
    __country_dropdown_locator = "div[class='products']>div>div>select"
    __terms_locator = "input[class='chkAgree']"
    __proceed = "//*[text()='Proceed']"
    __success_message_locator = "div[class='products']>div>span"
    __page_name = 'countrypage'

    def __init__(self):
        BaseClass.is_page_loaded(By.CSS_SELECTOR, self.__country_locator, self.__page_name)

    def select_terms_and_conditions(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__proceed)

    def click_on_proceed_button(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__terms_locator)

    def verify_order_success_message(self):
        message = "Thank you, your order has been placed successfully "
        text = BaseClass.get_element_text(By.CSS_SELECTOR, self.__success_message_locator)
        if message == text:
            return True
        else:
            return False

    def select_country(self, country_name):
        BaseClass.select_from_drop_down_by_text(By.CSS_SELECTOR, self.__country_dropdown_locator, text=country_name)
