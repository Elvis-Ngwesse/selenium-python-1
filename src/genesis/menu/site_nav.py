from selenium.webdriver.common.by import By

from helpers.utils import Context, get_config_key
from src.base.base_class import BaseClass


class SiteNavMenuPage:
    __help_locator = "(//*[text()='Help '])[2]"
    __site_pages = {'site_articles': '/resources/site-articles',
                    'authors': '/resources/authors'}
    __page_name = 'SiteNavMenuPage'

    def __init__(self):
        BaseClass.is_page_loaded(By.XPATH, self.__help_locator, self.__page_name)

    def navigate_page(self, page):
        BaseClass.navigate_to_link(f"{Context.url}{self.__site_pages[page]}")
