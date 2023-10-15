from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass


class OffersPage:
    __search_field = "input[id='search-field']"
    __vegetable_name = "table[class='table table-bordered']>tbody>tr>td:nth-child(1)"
    __vegetable_price = "table[class='table table-bordered']>tbody>tr>td:nth-child(2)"
    __vegetable_discount_price = "table[class='table table-bordered']>tbody>tr>td:nth-child(3)"
    __page_name = 'offerspage'

    def __init__(self):
        BaseClass.is_page_loaded(By.CSS_SELECTOR, self.__search_field, self.__page_name)

    def search_for_vegetable(self, vegetable_name: str):
        BaseClass.element_click(By.CSS_SELECTOR, self.__search_field)
        BaseClass.set_text(By.CSS_SELECTOR, self.__search_field, vegetable_name)

    def get_vegetable_name(self):
        veg_name = BaseClass.get_element_text(By.CSS_SELECTOR, self.__vegetable_name)
        return veg_name

    def get_vegetable_price(self):
        veg_price = BaseClass.get_element_text(By.CSS_SELECTOR, self.__vegetable_price)
        return int(veg_price)

    def get_vegetable_discount_price(self):
        veg_dis_price = BaseClass.get_element_text(By.CSS_SELECTOR, self.__vegetable_discount_price)
        return int(veg_dis_price)
