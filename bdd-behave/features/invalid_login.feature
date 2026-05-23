@negative
Feature: Invalid Login

  Scenario: Verify user cannot login with invalid mobile number

    Given User launches Myntra website
    When User opens login popup
    And User enters mobile number "12345"
    And User clicks consent checkbox
    And User clicks continue button
    Then Valid mobile number error should display

