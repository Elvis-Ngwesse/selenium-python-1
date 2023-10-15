from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass


class CartPage:
    __checkout_locator = "//*[text()='PROCEED TO CHECKOUT']"
    __amount = "(//p[@class='amount'])[1]"
    __price = "(//p[@class='product-price'])[1]"
    __page_name = 'cartpage'

    def __init__(self):
        BaseClass.is_page_loaded(By.CSS_SELECTOR, self.__checkout_locator, self.__page_name)

    def get_total_amount(self):
        results = BaseClass.get_element_text(By.CSS_SELECTOR, self.__amount)
        return results

    def get_unit_price(self):
        results = BaseClass.get_element_text(By.CSS_SELECTOR, self.__price)
        return results

    def click_on_checkout_button(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__checkout_locator)
