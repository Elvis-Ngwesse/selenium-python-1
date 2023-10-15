import time
from threading import Lock

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import allure
import pytest
from allure_commons import plugin_manager
from allure_pytest_bdd.pytest_bdd_listener import PytestBDDListener

from helpers.utils import add_tags_allure, add_links_allure, Context, load_yaml_file, get_config_key, get_time_stamp
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from pytest_harvest import saved_fixture
import os
import glob
from loguru import logger

from src.base.base_class import BaseClass

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "."))
driver = None


def interceptor(request):
    if request.url.startswith('https://kaxmedia.cloudflareaccess.com/'):
        request.create_response(
            status_code=302,
            # headers={'Content-Type': 'text/html'},  # Optional headers dictionary
            # body='<html>Hello World!</html>'
        )


@pytest.fixture(autouse=True)
@saved_fixture  # to save all instances created. access using fixture_store
def webdriver_setup(request):
    """
    Initialises test run
    :param request: Gets test Context
    """

    global driver
    global options

    # Load yaml file
    load_yaml_file()

    # Get values from Context
    headless = Context.config['Headless']
    grid = Context.config['Grid']
    gpu = Context.config['Gpu']
    maximized = Context.config['Maximized']
    detached = Context.config['Detach']
    headless = Context.config['Headless']
    remote_grid_url = Context.config['GridUrl']
    disable_extensions = Context.config['Disable_Extensions']
    disable_logging = Context.config['Disable_Logging']

    # Get values from config
    browser = get_config_key('Browsers')
    page_load_strategy = get_config_key('Page_Load_Strategy')
    Context.url = get_config_key('environment')

    try:
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
        if browser == 'firefox':
            options = webdriver.FirefoxOptions()

        if headless: options.add_argument('--headless')
        if gpu: options.add_argument('--disable-gpu')
        if maximized: options.add_argument('--start-maximized')
        if disable_extensions: options.add_argument('--disable-extensions')
        if disable_logging: options.add_argument('--disable-logging')
        options.page_load_strategy = page_load_strategy
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        options.add_argument(f"--user-agent={user_agent}")

        logger.info(f'Opening {browser} browser')
        if browser == 'chrome' and grid == False:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif browser == 'firefox' and grid == False:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == 'edge' and grid == False:
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        elif grid:
            if browser == 'chrome':
                options.add_argument('headless')
                options.add_argument('no-sandbox')
                options.add_argument('--selenium-manager true')
                driver = webdriver.Remote(command_executor=remote_grid_url,
                                          options=options)
            if browser == 'firefox':
                driver = webdriver.Remote(command_executor=remote_grid_url,
                                          options=webdriver.FirefoxOptions())
            if browser == 'edge':
                driver = webdriver.Remote(command_executor=remote_grid_url,
                                          options=webdriver.EdgeOptions())

        Context.driver = driver
        driver.set_script_timeout(120)
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        driver.delete_all_cookies()

        driver.get(Context.url)
        test_name = request.node.name  # Get current test name
        Context.test_name = test_name

        log_dir_allure = f'{ROOT_DIR}/allure/*'
        # Delete files from allure folder
        files = glob.glob(log_dir_allure)
        for f in files:
            os.remove(f)

        yield

        driver.quit()
        logger.info(f'Closing {browser} browser')
    except Exception as error:
        if driver:
            driver.quit()
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # Lock current thread execution
    lock = Lock()
    lock.acquire()

    if report.when == "call" and report.failed:
        log_dir_screenshots = f'{ROOT_DIR}/screenshots/*'
        # Delete files from screenshot folder
        files = glob.glob(log_dir_screenshots)
        for f in files:
            os.remove(f)
        BaseClass.take_screenshot(driver)
        for plugin in plugin_manager.list_name_plugin():
            p = plugin[1]
            if isinstance(p, PytestBDDListener):
                Context.test_result = p.lifecycle._get_item()
                add_tags_allure(item)
                add_links_allure()
                # add description to allure report
                Context.test_result.description = Context.test_result.name

    lock.release()
