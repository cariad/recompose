from pytest import raises

from recompose import InvalidSchema
from recompose.with_readers import WithCursorSchemaReader


def test_incorrect_type() -> None:
    with raises(InvalidSchema) as ex:
        WithCursorSchemaReader.get_required(
            {
                "cursor": "pizza",
            }
        )

    assert str(ex.value) == "Expected \"cursor\" to be dict but found 'pizza' (str)"


def test_missing() -> None:
    with raises(InvalidSchema) as ex:
        WithCursorSchemaReader.get_required({})

    assert str(ex.value) == '"cursor" is not present in schema (<none>)'
