from pytest import raises

from recompose import NotATransformerType, find_transformer


def test_find_transformer__none() -> None:
    with raises(NotATransformerType) as ex:
        find_transformer("pizza")

    assert str(ex.value) == "pizza is not a known transformer"
