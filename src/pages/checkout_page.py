from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass


class CheckoutPage:
    __checkout_table_locator = "[id='productCartTables']"
    __place_order_locator = "//*[text()='Place Order']"
    __apply_locator = "//*[text()='Apply']"
    __product_locator = "p[class='product-name']"
    __quantity_locator = "p[class='quantity']"
    __price_locator = "(//*[@class='amount'])[1]"
    __total_locator = "(//*[@class='amount'])[2]"
    __page_name = 'checkoutpage'

    def __init__(self):
        BaseClass.is_page_loaded(By.CSS_SELECTOR, self.__checkout_table_locator, self.__page_name)

    def click_on_place_order_button(self):
        BaseClass.element_click(By.XPATH, self.__place_order_locator)

    def click_on_apply_button(self):
        BaseClass.element_click(By.XPATH, self.__apply_locator)

    def get_product_name(self):
        results = BaseClass.get_element_text(By.CSS_SELECTOR, self.__product_locator)
        return results

    def get_quantity(self):
        results = BaseClass.get_element_text(By.CSS_SELECTOR, self.__quantity_locator)
        return results

    def get_total_amount(self):
        results = BaseClass.get_element_text(By.CSS_SELECTOR, self.__total_locator)
        return results

    def get_unit_price(self):
        results = BaseClass.get_element_text(By.CSS_SELECTOR, self.__product_locator)
        return results

