
@positive
Feature: Add Product To Bag

  Scenario: Verify user can add product to bag

    Given User launches Myntra website
    Then User verifies homepage successfully
    When User opens kids section
    Then User verifies kids page successfully
    When User searches for "Kids T-shirt"
    And User opens first product
    Then User verifies product page successfully
    When User selects product size
    And User adds product to bag
    Then User verifies product added successfully

