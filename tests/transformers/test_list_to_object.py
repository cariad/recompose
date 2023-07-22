from recompose.transformer_classes import ListToObject


def test_str() -> None:
    assert str(ListToObject()) == "list-to-object"
