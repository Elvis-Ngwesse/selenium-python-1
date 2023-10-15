from pytest_bdd import then, parsers, scenario

from helpers.utils import Context


@then(
    parsers.cfparse('I verify "{tomato}", "{price:Number}" and "{discount_price:Number}"', extra_types={"Number": int}))
def verify_tomato_is_selected(tomato, price, discount_price):
    offers_page = Context.offers_page
    name = offers_page.get_vegetable_name()
    _price = offers_page.get_vegetable_price()
    disc_price = offers_page.get_vegetable_discount_price()
    assert name == tomato
    assert _price == price
    assert disc_price == discount_price


@then(
    parsers.cfparse('I verify "{wheat}", "{price:Number}" and "{discount_price:Number}"', extra_types={"Number": int}))
def verify_wheat_is_selected(wheat, price, discount_price):
    offers_page = Context.offers_page
    name = offers_page.get_vegetable_name()
    _price = offers_page.get_vegetable_price()
    disc_price = offers_page.get_vegetable_discount_price()
    assert name == wheat
    assert _price == price
    assert disc_price == discount_price


@then('I verify page url')
def verify_page_url():
    offers_page_url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
    url = Context.url
    assert url == offers_page_url


@then('I verify quantity is correct')
def i_verify_results():
    results = Context.results
    assert results == 3


@then('I verify quantity is correct')
def i_verify_results():
    results = Context.results
    assert results == 5
