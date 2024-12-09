Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Background:
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"

Scenario: I can see the default inputs
    When I pause for 1000ms
    Then I expect that element "#decoder-setting" contains any text
    Then I expect that element "#shift-amount" contains the text "0"
    Then I expect that element "#letters" contains the text "when in rome, do as the romans do"

Scenario: I can successfully encode a secret message
    When I select the option with the value "E" for element "#decoder-setting"
    And I select the option with the text "3" for element "#shift-amount"
    And I set "System testing" to the inputfield "#letters"
    And I click on the button "#submit"
    And I pause for 200ms
    Then I expect that element "#decoded_message" contains the text "Vbvwhp whvwlqj"

Scenario: I can successfully decode a secret message
    When I select the option with the value "D" for element "#decoder-setting"
    And I select the option with the text "3" for element "#shift-amount"
    And I set "Vbvwhp whvwlqj" to the inputfield "#letters"
    And I click on the button "#submit"
    And I pause for 200ms
    Then I expect that element "#decoded_message" contains the text "System testing"

Scenario: I can get a suggestion on how to decode a secret message
    When I select the option with the value "D" for element "#decoder-setting"
    And I select the option with the text "0" for element "#shift-amount"
    And I set "Vbvwhp whvwlqj" to the inputfield "#letters"
    And I click on the button "#submit"
    And I pause for 200ms
    Then I expect that element "#suggested_solution" contains the text "3"

Scenario: I can clear the text box to type in a new message
    When I set "Vbvwhp whvwlqj" to the inputfield "#letters"
    And I click on the button "#reset"
    Then I expect that element "#letters" not contains the text "Vbvwhp whvwlqj"