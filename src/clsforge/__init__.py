__all__ = ("__version__", "FrozenClassError", "FrozenClassMeta", "EnumMixin")

from importlib import metadata

from clsforge.exceptions import FrozenClassError
from clsforge.meta import FrozenClassMeta
from clsforge.mixin import EnumMixin

__version__ = metadata.version(__name__)
