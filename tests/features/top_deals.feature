@regression
@smoke

Feature: Top Deals
  Background: navigate to page
    Given I navigate to GreenKart Page
    When  I click on top deals

  @deal
  Scenario: Make a new deal for tomatoes
      And   I navigate to offers page
      And   I search for vegetable "tomato"
      Then  I verify "Tomato", "37" and "26"

  @count
  Scenario: Make a new deal for wheat
      And   I navigate to offers page
      And   I search for vegetable "wheat"
      Then  I verify "Wheat", "67" and "28"

  @view
  Scenario: View offers
      And   I navigate to offers page and back
      Then  I verify page url