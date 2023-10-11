from pytest_bdd import given
from helpers.utils import Context
from src.common.cloudflare import CloudFlarePage
from src.genesis.pages.dashboard import DashboardsPage
from src.genesis.pages.loginpage import LoginPage


@given('I want to do something')
def do_something():
    pass


@given('I want to do something two')
def do_something():
    pass


@given('I want to do something three')
def do_something():
    dashboards_page = DashboardsPage()
    Context.dashboards_page = dashboards_page


@given("I navigate to Dashboard page")
def navigate_to_dashboard_page():
    dashboards_page = DashboardsPage()
    Context.dashboards_page = dashboards_page


@given("I navigate to cloudflare")
def open_genesis():
    cloudflare_page = CloudFlarePage()
    Context.cloudflare_page = cloudflare_page
    cloudflare_page.enter_user_email('elvis.ngwesse@gdcgroup.com')
    cloudflare_page.click_send_me_a_code_button()
    cloudflare_page.enter_code('151163')
    cloudflare_page.click_sign_button()


@given("I navigate to login page")
def navigate_to_login_page():
    login_page = LoginPage()
    Context.login_page = login_page


@given("I login with username and password")
def login_user():
    username = Context.config['test_User']['User_2'][0]['username']
    password = Context.config['test_User']['User_2'][1]['password']

    login_page = Context.login_page
    login_page.enter_user_email(email=username)
    login_page.enter_user_password(password=password)
    login_page.select_remember_me_checkbox()
    login_page.click_on_login_button()
