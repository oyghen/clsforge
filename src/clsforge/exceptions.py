__all__ = ["ClsForgeError", "FrozenClassError", "InvalidChoiceError"]

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


class ClsForgeError(Exception): ...


class FrozenClassError(ClsForgeError, TypeError): ...


class InvalidChoiceError(ClsForgeError, ValueError):
    """Raised when a value is not one of the allowed choices."""

    def __init__(self, value: T, choices: Sequence[T]) -> None:
        super().__init__(f"invalid value {value!r}: expected one of {choices!r}")
