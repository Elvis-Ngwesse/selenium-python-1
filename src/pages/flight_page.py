from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass

class FlightPage:
    __book_flight_locator = "li[class='book_flight']"
    __page_name = 'flightpage'

    def __init__(self):
        BaseClass.is_page_loaded(By.CSS_SELECTOR, self.__book_flight_locator, self.__page_name)