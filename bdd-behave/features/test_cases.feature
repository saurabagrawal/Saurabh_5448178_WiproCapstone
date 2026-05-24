Feature: Myntra Positive And Negative Test Cases


  @positive
  Scenario: Verify add product to bag successfully

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


  @positive
  Scenario: Verify brand filter functionality

    Given User launches Myntra website

    Then User verifies homepage successfully

    When User opens kids section

    Then User verifies kids page successfully

    When User searches for "Girls Tops"

    And User applies brand filter

    Then Brand filter should apply successfully


  @positive
  Scenario: Verify product details page

    Given User launches Myntra website

    Then User verifies homepage successfully

    When User opens kids section

    Then User verifies kids page successfully

    When User searches for "Kids T-shirt"

    And User opens first product

    Then User verifies product page successfully


  @positive
  Scenario: Verify valid login functionality

    Given User launches Myntra website

    When User opens login popup

    And User enters mobile number "9152358202"

    And User clicks consent checkbox

    And User clicks continue button

    Then OTP page should display successfully


  @negative
  Scenario: Verify invalid login functionality

    Given User launches Myntra website

    When User opens login popup

    And User enters mobile number "12345"

    And User clicks consent checkbox

    And User clicks continue button

    Then Valid mobile number error should display


  @negative
  Scenario: Verify invalid product search functionality

    Given User launches Myntra website

    Then User verifies homepage successfully

    When User opens kids section

    Then User verifies kids page successfully

    When User searches for "asdkjasdhj"

    Then No products should display