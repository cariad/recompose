from pytest import raises

from recompose import NoCursorForCondition, UnsupportedVersion, make_cursor


def test_make_cursor__none() -> None:
    with raises(NoCursorForCondition) as ex:
        make_cursor(
            {
                "on": "each-pizza",
                "perform": [],
            },
            require_version=False,
        )

    assert str(ex.value) == 'No cursors can satisfy condition "each-pizza"'


def test_version__none() -> None:
    with raises(UnsupportedVersion) as ex:
        make_cursor(
            {
                "on": "each-value",
                "perform": [],
            },
        )

    expect = (
        "Schema does not describe its version " "({'on': 'each-value', 'perform': []})"
    )

    assert str(ex.value) == expect


def test_version__not_integer() -> None:
    with raises(UnsupportedVersion) as ex:
        make_cursor(
            {
                "on": "each-value",
                "perform": [],
                "version": "1",  # type: ignore
            },
        )

    assert str(ex.value) == "Schema version '1' (str) is not an integer"


def test_version__later() -> None:
    with raises(UnsupportedVersion) as ex:
        make_cursor(
            {
                "on": "each-value",
                "perform": [],
                "version": 999,
            },
        )

    assert str(ex.value) == "Found schema version 999 but expected no later than 1"
