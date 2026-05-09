from clsforge import InvalidChoiceError


class TestInvalidChoiceError:
    def test_valid_choice__list(self):
        exc = InvalidChoiceError(choice=0, choices=[1, 2, 3])
        assert str(exc) == "invalid choice 0: expected one of [1, 2, 3]"

    def test_valid_choice__tuple(self):
        exc = InvalidChoiceError(choice=0, choices=(1, 2, 3))
        assert str(exc) == "invalid choice 0: expected one of (1, 2, 3)"

    def test_valid_choice__set(self):
        exc = InvalidChoiceError(choice=0, choices={1, 2, 3})
        assert str(exc) == "invalid choice 0: expected one of {1, 2, 3}"
