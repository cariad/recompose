from pytest import mark, raises

from recompose import InvalidSchema
from recompose.schema_readers import PathReader
from recompose.types import TransformSchema


def test_incorrect_type() -> None:
    with raises(InvalidSchema) as ex:
        PathReader.get_required(
            {
                "path": 0,
            }
        )

    assert str(ex.value) == 'Expected "path" to be str but found 0 (int)'


@mark.parametrize(
    "args",
    [
        {},
        {"foo": "bar"},
    ],
)
def test_optional(args: TransformSchema) -> None:
    assert PathReader.get_optional(args) is None
