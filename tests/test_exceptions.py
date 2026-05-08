from clsforge import InvalidChoiceError


def test_invalid_choice_error():
    exc = InvalidChoiceError(choice=0, choices=[1, 2, 3])
    assert str(exc) == "invalid choice 0: expected one of [1, 2, 3]"
