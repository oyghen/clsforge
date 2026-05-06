import pytest

from clsforge import FrozenClassError, FrozenClassMeta


class BaseClass(metaclass=FrozenClassMeta):
    A = 1
    B = "x"


class SubClass(BaseClass):
    C = 3


class TestFrozenClassMeta:
    def test_attributes_accessible(self):
        assert BaseClass.A == 1
        assert BaseClass.B == "x"

    def test_cannot_set_attribute(self):
        with pytest.raises(FrozenClassError) as exc:
            BaseClass.A = 2  # type: ignore

        msg = str(exc.value)
        assert "Cannot set field 'A'" in msg
        assert "BaseClass" in msg
        assert "2" in msg

    def test_cannot_add_new_attribute(self):
        with pytest.raises(FrozenClassError) as exc:
            BaseClass.NEW = 123

        msg = str(exc.value)
        assert "Cannot set field 'NEW'" in msg
        assert "123" in msg

    def test_cannot_delete_attribute(self):
        with pytest.raises(FrozenClassError) as exc:
            del BaseClass.A

        msg = str(exc.value)
        assert "Cannot delete field 'A'" in msg
        assert "BaseClass" in msg

    def test_subclass_inherits_attributes(self):
        assert SubClass.A == 1
        assert SubClass.C == 3

    def test_subclass_is_also_immutable(self):
        with pytest.raises(FrozenClassError):
            SubClass.C = 10  # type: ignore

        with pytest.raises(FrozenClassError):
            SubClass.NEW = "fail"

    def test_cannot_instantiate(self):
        with pytest.raises(FrozenClassError) as exc:
            BaseClass()

        msg = str(exc.value)
        assert "Cannot instantiate frozen class" in msg
        assert "BaseClass" in msg

    def test_namespace_is_copied_on_creation(self):
        namespace = {"X": 1}

        class Temp(metaclass=FrozenClassMeta):
            X = namespace["X"]

        namespace["X"] = 999
        assert Temp.X == 1

    def test_error_message_contains_class_name(self):
        with pytest.raises(FrozenClassError) as exc:
            BaseClass.A = 5  # type: ignore

        assert "BaseClass" in str(exc.value)

    def test_dir_still_lists_attributes(self):
        attrs = dir(BaseClass)
        assert "A" in attrs
        assert "B" in attrs

    def test_type_setattr_can_bypass_freeze(self):
        # Documented limitation: direct type.__setattr__ bypasses metaclass protection
        assert BaseClass.A == 1
        type.__setattr__(BaseClass, "A", 999)
        assert BaseClass.A == 999

    def test_subclass_definition_still_works(self):
        class AnotherSubClass(BaseClass):
            D = 4

        assert AnotherSubClass.D == 4

    def test_multiple_inheritance_compatibility(self):
        class Mixin:
            @classmethod
            def method(cls):
                return "ok"

        class Combined(BaseClass, Mixin):
            E = 5

        assert Combined.E == 5
        assert Combined.method() == "ok"

        with pytest.raises(FrozenClassError):
            SubClass.E = 10  # type: ignore
