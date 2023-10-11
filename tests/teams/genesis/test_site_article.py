import pytest
from pytest_bdd import scenario
from helpers.file_reader import *
from steps.genesis_steps.given import *
from steps.genesis_steps.when import *
from steps.genesis_steps.then import *

feature_file_path = lambda file_name: f'../../features/genesis/{file_name}'


@pytest.mark.case_id('2105')
@scenario('../../features/genesis/navigate_to_dashboard.feature', 'Dashboard page')
def test_site_article():
    pass


@pytest.mark.case_id('2106')
@scenario(feature_file_path('sample_feature.feature'), 'Random Scenario')
def test_random():
    pass


@pytest.mark.case_id('2107')
@scenario(feature_file_path('feature_two.feature'), 'Random Scenario two')
def test_random_two():
    pass


@pytest.mark.case_id('2108')
@scenario(feature_file_path('third_feature.feature'), 'Random Scenario three')
def test_random_three():
    pass
