from pytest_bdd import when
from src.genesis.menu.site_nav import SiteNavMenuPage


@when('I do the thing')
def random_function():
    pass


@when('I navigate to Site Articles Page')
def navigate_to_site_articles():
    site_nav = SiteNavMenuPage()
    site_nav.navigate_page(page='site_articles')


@when('I do the thing three')
def random_function():
    pass


@when("I do the thing two")
def step_impl():
    pass