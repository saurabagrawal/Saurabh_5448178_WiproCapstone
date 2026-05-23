@negative
Feature: Invalid Product Search

  Scenario: Verify user cannot search invalid product

    Given User launches Myntra website
    Then User verifies homepage successfully
    When User opens kids section
    Then User verifies kids page successfully
    When User searches for "asdkjasdhj"
    Then No products should display

