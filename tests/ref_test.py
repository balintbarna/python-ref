# external
from typing import Any
from pytest import raises
# local
from refcontainer import Ref, ReadOnlyError


def test_starting_value():
    str_ref = Ref('hello')
    assert str_ref.current == 'hello'


def test_overwrite():
    str_ref = Ref('hello')
    str_ref.current = 'world'
    assert str_ref.current == 'world'


def test_delete():
    str_ref = Ref('hello')
    del str_ref.current
    with raises(AttributeError):
        _ = str_ref.current
    str_ref.current = 'world'
    assert str_ref.current == 'world'


def test_engrave():
    str_ref = Ref('')
    str_ref.engrave('hello')
    with raises(ReadOnlyError):
        str_ref.current = 'world'
    with raises(ReadOnlyError):
        del str_ref.current
    with raises(ReadOnlyError):
        str_ref.engrave('world')
    assert str_ref.current == 'hello'


def test_readonly():
    str_ref = Ref.readonly('hello')
    with raises(ReadOnlyError):
        del str_ref.current
    assert str_ref.current == 'hello'


def test_type_change():
    str_ref = Ref('hello')
    with raises(TypeError):
        str_ref.current = 0


def test_tagged():
    ref = Ref[str | int]('hello')
    assert ref.current == 'hello'
    ref.current = 'world'
    ref.current = 0
    with raises(TypeError):
        ref.current = 0.


def test_any():
    ref = Ref[Any]('hello')
    assert ref.current == 'hello'
    ref.current = 0
    ref.current = 0.


def test_empty_constructor():
    num_ref = Ref[float]()
    with raises(AttributeError):
        _ = num_ref.current
    num_ref.current = 0.
    assert num_ref.current == 0
    with raises(TypeError):
        num_ref.current = 'hello'
