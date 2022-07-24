Feature: Free CRM Login Feature

  Scenario: Login Scenario
    Given I navigate to Free CRN login Page having url "https://freecrm.com/"
    When I click on login button
    And I provide username as "admin"
    And I provide password as "admin123"
    And I click on login button
    Then I verify that homepage is open

  Scenario Outline: Login Scenario
    Given I navigate to Free CRN login Page having url "url"
    When I click on login button
    And I provide username as "username"
    And I provide password as "password"
    And I click on login button
    Then I verify that homepage is open with title is "title_is_this"

    Examples:
      |url                 |username|password|title_is_this|
      |https://freecrm.com/|admin   |admin123|eng_title    | 1.1
      |https://freecrm.com/|sgssd   |admin456|1.2
      |https://freecrm.com/|admim   |admin789|