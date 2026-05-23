@positive
Feature: Product Details

  Scenario: Verify user can open product details

    Given User launches Myntra website
    Then User verifies homepage successfully
    When User opens kids section
    Then User verifies kids page successfully
    When User searches for "Kids T-shirt"
    And User opens first product
    Then User verifies product page successfully

