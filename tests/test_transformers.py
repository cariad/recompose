from pytest import raises

from recompose import NotATransformerType, find_transformer


def test_find_transformer__none() -> None:
    with raises(NotATransformerType) as ex:
        find_transformer({"transform": "pizza"})

    assert str(ex.value) == 'No registered transformers named "pizza"'
