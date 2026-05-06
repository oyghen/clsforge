__all__ = ["FrozenClassMeta"]


from clsforge import FrozenClassError


class FrozenClassMeta(type):
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
