from recompose.cursor_classes import ThisValue


def test_str() -> None:
    transformer = ThisValue(
        {
            "on": "this-value",
            "perform": [],
        }
    )

    assert str(transformer) == "this-value"
