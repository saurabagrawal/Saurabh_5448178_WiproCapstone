@positive
Feature: Valid Login

  Scenario: Verify valid login flow

    Given User launches Myntra website
    When User opens login popup
    And User enters mobile number "9152358202"
    And User clicks consent checkbox
    And User clicks continue button
    Then OTP page should display successfully

