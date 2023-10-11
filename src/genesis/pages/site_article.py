from selenium.webdriver.common.by import By

from helpers.utils import Context
from src.base.base_class import BaseClass


class SiteArticlePage:

    __title_locator = "//*[text()='Title ']"
    __create_site_article_locator = "//*[text()='Create Site Article']"
    __page_name = 'SiteArticlePage'

    def __init__(self):
        BaseClass.is_page_loaded(By.XPATH, self.__title_locator, self.__page_name)

    def click_on_create_site_article_button(self):
        BaseClass.element_click(By.XPATH, self.__create_site_article_locator)


