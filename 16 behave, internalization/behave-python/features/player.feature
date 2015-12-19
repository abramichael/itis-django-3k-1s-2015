Feature: Player behavior

  Scenario: Initialization
    Given a new player
    then he should have name
    and he should have hp
    and his hp should be 100

  Scenario: Kicking
    Given two players
    when first kicks second with power 10
    then second's hp decrease on 10