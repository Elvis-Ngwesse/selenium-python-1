@regression
@smoke
Feature: Go to Dashboard page

  Background:
    Given I navigate to login page
    And   I login with username and password

  Scenario: Dashboard page
    When I navigate to Site Articles Page
    Then Thing is done two