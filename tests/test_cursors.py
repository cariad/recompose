from pytest import raises

from recompose import NoCursorAvailable, find_cursor


def test_find_cursor__none() -> None:
    with raises(NoCursorAvailable) as ex:
        find_cursor({"foo": "bar"})

    assert str(ex.value) == "No cursors support this template ({'foo': 'bar'})"
