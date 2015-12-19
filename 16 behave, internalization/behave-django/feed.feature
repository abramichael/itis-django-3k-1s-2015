Feature: Feed

  Scenario Outline: Anon and Feed

    Given a new authorized user
	Then he has access to <page>

    Examples: urls for authorized
    |page	  |
    |/feed    |
    |/feed/hello|