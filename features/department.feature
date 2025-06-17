Feature: Manage Departments

  Background:
    Given a user exists and is authenticated
    And a department named "HR" exists
    Then the user should be authenticated

  Scenario: Create a new department
    When I POST to "/api/v1/departments/" with name "HR":
    Then the response status should be 201
    And the response should contain "HR"

  Scenario: List departments
    When I GET "/api/v1/departments/"
    Then the response status should be 200
    And the response should contain "HR"

  Scenario: Update a department
    When I PUT "/api/v1/departments" with name "Finance":
    Then the response status should be 200
    And the response should contain "Finance"

  Scenario: Delete a department
    When I DELETE "/api/v1/departments"
    Then the response status should be 204

  Scenario: Try to get a non-existing department
    When I GET "/api/v1/departments/999/"
    Then the response status should be 404
    And the response should contain "Not found"

  Scenario: List departments when none exist
    Given the departments table is empty
    When I GET "/api/v1/departments/"
    Then the response status should be 200
    And the response should contain "results"
