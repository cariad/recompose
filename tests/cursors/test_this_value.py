from recompose.cursor_classes import ThisValue


def test_str() -> None:
    assert str(ThisValue({})) == "this-value"
