from selenium.webdriver.common.by import By
from src.base.base_class import BaseClass


class DashboardsPage:
    __documentation_locator = "//*[text()='Documentation']"
    __page_name = 'DashboardsPage'

    def __init__(self):
        BaseClass.is_page_loaded(By.XPATH, self.__documentation_locator, self.__page_name)

