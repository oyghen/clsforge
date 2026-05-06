__all__ = ("__version__", "FrozenClassError", "FrozenClassMeta", "EnumMixin")

from importlib import metadata

__version__ = metadata.version(__name__)


from clsforge.exceptions import FrozenClassError
from clsforge.meta import FrozenClassMeta
from clsforge.mixin import EnumMixin
