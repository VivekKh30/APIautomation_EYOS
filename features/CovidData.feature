Feature: Validation of GET Covid-19 data using Country Code endpoint

  Scenario Outline: Retrieve Covid-19 data using getLatestCountryDataByCode endpoint
    Given Request is sent to GET Covid-19 data with <code>
    Then response is received with HTTP status code 200
    And the response body should return expected details as below
      | country   | code   | latitude   | longitude   |
      | <country> | <code> | <latitude> | <longitude> |
    Examples:
      | code | country | latitude  | longitude |
      | IT   | Italy   | 41.87194  | 12.56738  |
      | IN   | India   | 20.593684 | 78.96288  |
      | GB   | UK      | 55.378051 | -3.435973 |


  Scenario: Validate response when empty country code is passed
    When Request is sent to GET Covid-19 data without country code
    Then response is received with HTTP status code 200
    And the empty response body should be returned

  Scenario Outline: Validate response when invalid country code is passed
    When Request is sent to GET Covid-19 data with invalid "<country_code>"
    Then response is received with HTTP status code 400
    And response should contain an error message as "Invalid country code"
    Examples:

      | country_code |
      | 123          |
      | @432         |
      | INDI         |

  Scenario: Validate response when request is sent without an API key
    When Request is sent to GET Covid-19 data without an API key
    Then response is received with HTTP status code 401
    And response should contain an error message as "Invalid API key. Go to https://docs.rapidapi.com/docs/keys for more info."

  Scenario: Validate response when request is sent with an invalid API key
    When Request is sent to GET Covid-19 data with an invalid API key
    Then response is received with HTTP status code 403
    And response should contain an error message as "You are not subscribed to this API."


  Scenario: Validate response when request is sent without mandatory query parameter
    When Request is sent to GET Covid-19 data without query parameter
    Then response is received with HTTP status code 400
    And response should contain an error message as "Bad Request"


  Scenario Outline: Validate that number of confirmed cases of India is more than Italy
    Given Request is sent to GET Covid-19 data for <code> and <code2>
    Then  response is received with HTTP status code 200
    And Number of confirmed cases for IN should be greater than IT
    Examples:
      | code | code2 |
      | IN   | IT    |





