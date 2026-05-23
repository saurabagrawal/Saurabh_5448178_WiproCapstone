@positive
Feature: Brand Filter

  Scenario: Verify user can apply brand filter

    Given User launches Myntra website
    Then User verifies homepage successfully
    When User opens kids section
    Then User verifies kids page successfully
    When User applies brand filter
    Then Brand filter should apply successfully

