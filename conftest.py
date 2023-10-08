from os.path import exists
import allure
import pytest
from allure_commons import plugin_manager
from allure_pytest_bdd.pytest_bdd_listener import PytestBDDListener
from helpers.utils import add_tags_allure, add_links_allure, Context, load_yaml_file, get_config_key, get_time_stamp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from pytest_harvest import saved_fixture
import os
import glob
from loguru import logger

from src.base.base_class import BaseClass
from src.genesis.pages.dashboard import DashboardsPage
from src.genesis.pages.site_article import SiteArticlePage

driver = None


@pytest.fixture(autouse=True)
@saved_fixture  # to save all instances created. access using fixture_store
def webdriver_setup(request):
    """
    Initialises test run
    :param request: Gets test Context
    """

    global driver

    # Load yaml file
    load_yaml_file()

    try:
        options = Options()
        options.headless = Context.config['Headless']
        browser = get_config_key('Browsers')
        remote_grid_url = Context.config['GridUrl']
        logger.info(f'Opening {browser} browser')
        if browser == 'chrome':
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif browser == 'firefox':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser == 'safari':
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser == 'edge':
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        elif browser == 'grid':
            options.headless = True
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Remote(command_executor=remote_grid_url,
                                      options=webdriver.ChromeOptions())
        Context.driver = driver
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        url = get_config_key('environment')
        driver.get(url)
        test_name = request.node.name  # Get current test name
        Context.test_name = test_name
        _dir = os.getcwd()
        log_dir = _dir.replace('tests', 'screenshots/*')
        # Delete files from screenshot folder
        files = glob.glob(log_dir)
        for f in files:
            os.remove(f)

        yield
        driver.quit()
        logger.info(f'Closing {browser} browser')
    except Exception as error:
        logger.error(error)
        raise error


def pytest_bdd_before_scenario(request, feature, scenario):
    Context.pytest_bdd_step_error = False


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # Attaches logs and screenshots to allure reports in case of failure
    Context.pytest_bdd_step_error = True
    _dir = os.getcwd().replace('tests', 'screenshots')
    time_stamp = get_time_stamp()
    file_exists = os.path.exists(f'{_dir}/{Context.test_name}.png')
    if file_exists:
        allure.attach.file(source=f'{_dir}/{Context.test_name}.png', name=f'{Context.test_name}.{time_stamp}',
                           attachment_type=allure.attachment_type.PNG)


def pytest_bdd_after_scenario(request, feature, scenario):
    # Attaches log to allure reports in case of failure
    if Context.pytest_bdd_step_error is True:
        allure.attach.file(source='pytest.log', name='log',
                           attachment_type=allure.attachment_type.TEXT)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        for plugin in plugin_manager.list_name_plugin():
            p = plugin[1]
            if isinstance(p, PytestBDDListener):
                Context.test_result = p.lifecycle._get_item()
                add_tags_allure(item)
                add_links_allure()
                # add description to allure report
                Context.test_result.description = Context.test_result.name


# Initialize page objects

@pytest.fixture()
def navigate_to_site_article_page():
    site_article_page = SiteArticlePage()
    Context.site_article_page = site_article_page


@pytest.fixture()
def navigate_to_dashboards_page():
    dashboards_page = DashboardsPage()
    Context.dashboards_page = dashboards_page
