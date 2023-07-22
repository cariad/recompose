from recompose.transformers.list_to_object import ListToObject


def test_str() -> None:
    assert str(ListToObject()) == "list-to-object"
