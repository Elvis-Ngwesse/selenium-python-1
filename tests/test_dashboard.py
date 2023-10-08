import pytest
from pytest_bdd import scenario
from steps.when import *
from steps.given import *
from steps.then import *
from helpers.file_reader import *

navigate_to_dashboard_feature = get_feature_file_path('navigate_to_dashboard')


@pytest.mark.case_id('2105')
@scenario(navigate_to_dashboard_feature, 'Dashboard page')
def test_dashboard():
    pass


@pytest.mark.case_id('2106')
@scenario('features/sample_feature.feature', 'Random Scenario')
def test_random():
    assert 2 + 2 == 4


@pytest.mark.case_id('2107')
@scenario('features/feature_two.feature', 'Random Scenario two')
def test_random_two():
    pass


@pytest.mark.case_id('2108')
@scenario('features/third_feature.feature', 'Random Scenario three')
def test_random_three():
    pass
