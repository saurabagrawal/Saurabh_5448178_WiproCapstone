@e2e
Feature: Myntra Complete Shopping Workflow

  Scenario Outline: User completes complete shopping and checkout workflow

    Given User launches Myntra website in e2e

    Then User verifies homepage successfully in e2e

    When User opens kids section in e2e

    Then User verifies kids page successfully in e2e

    When User searches for "<product>" in e2e

    And User opens first product in e2e

    Then User verifies product page successfully in e2e

    When User selects product size in e2e

    And User adds product to bag in e2e

    Then User verifies product added successfully in e2e

    When User opens shopping bag in e2e

    Then User verifies cart page successfully in e2e

    When User changes quantity to "<quantity>" in e2e

    And User selects donation "<donation>" in e2e

    And User clicks place order in e2e

    Then User should be redirected to login page in e2e

    When User enters mobile number "9152358202" in e2e

    And User clicks consent checkbox in e2e

    And User clicks continue button in e2e

    Then OTP page should display successfully in e2e


    Examples:
      | product        | quantity | donation |
      | Kids T-shirt   | 2        | 10       |
      | Boys Jeans     | 2        | 10       |