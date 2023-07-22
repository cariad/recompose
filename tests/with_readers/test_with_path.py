from typing import Optional

from pytest import mark, raises

from recompose import InvalidSchema
from recompose.types import WithArgs
from recompose.with_readers import WithPathReader


def test_incorrect_type() -> None:
    with raises(InvalidSchema) as ex:
        WithPathReader.get_required(
            {
                "path": 0,
            }
        )

    assert str(ex.value) == 'Expected "path" to be str but found 0 (int)'


@mark.parametrize(
    "args",
    [
        None,
        {},
        {"foo": "bar"},
    ],
)
def test_optional(args: Optional[WithArgs]) -> None:
    assert WithPathReader.get_optional(args) is None
