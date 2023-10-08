from pytest_bdd import given
from helpers.utils import Context


@given('I want to do something')
def do_something():
    pass


@given('I want to do something two')
def do_something():
    pass


@given('I want to do something three')
def do_something(navigate_to_dashboards_page):
    dashboards_page = Context.dashboards_page


@given("I navigate to Dashboard page")
def navigate_to_dashboard_page(navigate_to_dashboards_page):
    dashboards_page = Context.dashboards_page


@given("I open genesis")
def open_genesis():
    pass
