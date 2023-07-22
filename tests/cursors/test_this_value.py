from recompose.cursors.this_value import ThisValue


def test_str() -> None:
    assert str(ThisValue({})) == "this-value"
