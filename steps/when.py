from pytest_bdd import when, parsers, scenario

from helpers.utils import Context


@when('I click on top deals')
def click_on_top_deals():
    green_kart_page = Context.green_kart_page
    green_kart_page.click_on_top_deals()


@when('I navigate to offers page')
def navigate_to_offers_page():
    green_kart_page = Context.green_kart_page
    Context.offers_page = green_kart_page.navigate_to_offers_page()


@when(parsers.cfparse('I search for vegetable "{tomato}"'))
def search_for_tomato(tomato):
    offers_page = Context.offers_page
    offers_page.search_for_vegetable(vegetable_name=tomato)
    Context.offers_page = offers_page


@when(parsers.cfparse('I search for vegetable "{wheat}"'))
def search_for_wheat(wheat):
    offers_page = Context.offers_page
    offers_page.search_for_vegetable(vegetable_name=wheat)
    Context.offers_page = offers_page


@when('I navigate to offers page and back')
def navigate_to_offers_page():
    green_kart_page = Context.green_kart_page
    url = green_kart_page.navigate_to_offers_page_and_back()
    Context.url = url


@when('I increase vegetable quantity count')
def increase_brocolli_count():
    green_kart_page = Context.green_kart_page
    _brocolli = 'brocolli'
    results = green_kart_page.increase_item_quantity(_brocolli, _index=1, times=2)
    Context.results = results


@when('I increase vegetable quantity count')
def increase_cauliflower_count():
    green_kart_page = Context.green_kart_page
    _brocolli = 'cauliflower'
    results = green_kart_page.increase_item_quantity_by_double_clicking(_brocolli, _index=2, times=2)
    Context.results = results


@when('I navigate to required page')
def navigate_to_page():
    pass
