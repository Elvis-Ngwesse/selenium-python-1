import pytest
from pytest_bdd import scenario
from steps.given import *
from steps.when import *
from steps.then import *


@pytest.mark.case_id('2108')
@scenario('features/top_deals.feature', 'Make a new deal for tomatoes')
def test_get_tomato_deal():
    pass


@scenario('features/count.feature', 'Verify cauliflower count')
def test_verify_cauliflower_count():
    pass


@pytest.mark.case_id('2108')
@scenario('features/count.feature', 'Verify page one')
def test_always_pass_one():
    pass


@scenario('features/count.feature', 'Verify page two')
def test_always_pass_two():
    pass
