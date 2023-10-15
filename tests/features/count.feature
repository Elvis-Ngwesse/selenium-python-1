@regression
Feature: Vegetable Count

  Background: Navigate to page
    Given I navigate to GreenKart Page

  Scenario: Verify brocolli count
    When  I increase vegetable quantity count
    Then  I verify quantity is correct

 Scenario: Verify cauliflower count
    When  I increase vegetable quantity count
    Then  I verify quantity is correct

Scenario: Verify page one
    When  I navigate to required page

Scenario: Verify page two
    When  I navigate to required page
