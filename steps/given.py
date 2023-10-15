from pytest_bdd import given
from helpers.utils import Context
from src.pages.green_cart_page import GreenKartPage


@given("I navigate to GreenKart Page")
def navigate_to_green_kart_page():
    green_kart_page = GreenKartPage()
    Context.green_kart_page = green_kart_page
