from clsforge import InvalidChoiceError


def test_invalid_choice_error():
    exc = InvalidChoiceError(value=0, choices=[1, 2, 3])
    assert str(exc) == "invalid value 0: expected one of [1, 2, 3]"
