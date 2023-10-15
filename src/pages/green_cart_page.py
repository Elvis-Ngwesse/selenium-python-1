from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass
from src.pages.offers_page import OffersPage


class GreenKartPage:
    __green_kart = "//*[text()='Accept all']"
    __top_deal = "a[href='#/offers']"
    __flight_booking = "a[href*='dropdownsPractise/']"
    __cart_icon = "a[class='cart-icon']"
    __page_name = 'greenkartpage'

    def __init__(self):
        BaseClass.is_page_loaded(By.XPATH, self.__green_kart, self.__page_name)

    def click_on_top_deals(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__top_deal)

    def click_on_book_me_a_flight(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__flight_booking)

    def click_on_cart(self):
        BaseClass.element_click(By.CSS_SELECTOR, self.__cart_icon)

    def click_on_add_to_cart_button(self, index: int):
        add_cart = lambda _index: f"div[class='products-wrapper']>div>div:nth-child({_index})>div[class='product-action']>button"
        BaseClass.element_click(By.CSS_SELECTOR, add_cart(_index=index))

    def navigate_to_offers_page(self):
        BaseClass.switch_to_new_window(1)
        offers_page = OffersPage()
        return offers_page

    def navigate_to_offers_page_and_back(self):
        page_url = BaseClass.switch_to_new_window_and_back(window_before=0, window_after=1)
        return page_url

    def increase_item_quantity(self, vegetable: str, _index: int, times: int = 0):
        locator = self.__get_vegetable_locator(vegetable=vegetable)
        index_locator = self.__get_increment_index(_index)
        BaseClass.element_hover_over(By.CSS_SELECTOR, locator)
        [BaseClass.element_click(By.XPATH, index_locator) for _ in range(times)]
        value = self.__get_quantity(_index)
        return value

    def increase_item_quantity_by_double_clicking(self, vegetable: str, _index: int, times: int = 0):
        locator = self.__get_vegetable_locator(vegetable=vegetable)
        index_locator = self.__get_increment_index(_index)
        BaseClass.element_hover_over(By.CSS_SELECTOR, locator)
        [BaseClass.double_click(By.XPATH, index_locator) for _ in range(times)]
        value = self.__get_quantity(_index)
        return value

    def __get_vegetable_locator(self, vegetable):
        _vegetable = lambda vegetable_name: f"img[alt*='{vegetable_name}']"
        string_locator = _vegetable(vegetable_name=vegetable.capitalize())
        return string_locator

    def __get_increment_index(self, index):
        _increment = lambda increment_index: f"(//a[@class='increment'])[{increment_index}]"
        _index = _increment(increment_index=index)
        return _index

    def __get_quantity(self, index):
        _quantity = lambda quantity_index: f"(//div[@class='stepper-input']//input)[{quantity_index}]"
        string_locator = _quantity(quantity_index=index)
        _value = BaseClass.attribute_value(By.XPATH, string_locator, 'value')
        return int(_value)
