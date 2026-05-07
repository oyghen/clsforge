__all__ = ["FrozenClassMeta"]


from clsforge import FrozenClassError


class FrozenClassMeta(type):
    """Metaclass for immutable class definitions.

    Examples
    --------
    >>> class UserTable(metaclass=FrozenClassMeta):
    ...     NAME = "users"
    ...     PRIMARY_KEY = "id"
    ...
    >>> UserTable.NAME
    'users'
    >>> UserTable.PRIMARY_KEY
    'id'
    >>> UserTable.PRIMARY_KEY = "user_id"  # doctest: +SKIP
    Traceback (most recent call last):
        ...
    FrozenClassError
    """

    def __call__(cls, *args, **kwargs):
        raise FrozenClassError(
            f"Cannot instantiate frozen class '{cls.__name__}'. "
            f"Frozen classes are class-only definitions and do not support instances."
        )

    def __setattr__(cls, key, value):
        raise FrozenClassError(
            f"Cannot set field '{key}' to {value!r} on frozen class '{cls.__name__}'. "
            f"Frozen classes are immutable after class creation."
        )

    def __delattr__(cls, key):
        raise FrozenClassError(
            f"Cannot delete field '{key}' from frozen class '{cls.__name__}'. "
            f"Frozen classes are immutable after class creation."
        )

    def __new__(mcls, name, bases, namespace):
        return super().__new__(mcls, name, bases, dict(namespace))
