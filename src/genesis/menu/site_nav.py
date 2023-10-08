from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass


class SiteNavMenuPage:

    __title_locator = "//*[text()='Title ']"

    def __init__(self):
        BaseClass.is_page_loaded(By.XPATH, self.__title_locator)

