from pathlib import Path
from typing import Any, Optional

from pytest import mark, raises
from ruamel.yaml import YAML

from recompose import transform
from recompose.exceptions import PathNotFound
from recompose.options import Options

test_data = Path() / "tests" / "data"
yaml = YAML(typ="safe")


def load(id: int, dir: str) -> Any:
    padded_id = str(id).rjust(3, "0")
    path = test_data / dir / f"{padded_id}.yml"

    with open(path, "r") as f:
        return yaml.load(f)


@mark.parametrize(
    "cursor_id, data_id, expectation_id, options",
    [
        (0, 0, 0, None),
        (1, 1, 1, None),
        (2, 2, 2, None),
        (3, 3, 3, None),
        (4, 3, 3, None),
        (5, 0, 0, None),
        (6, 3, 3, None),
        (7, 3, 4, Options(allow_missing_data=True)),
    ],
)
def test(
    cursor_id: int,
    data_id: int,
    expectation_id: int,
    options: Optional[Options],
) -> None:
    schema = load(cursor_id, "cursors")
    data = load(data_id, "data")
    expectation = load(expectation_id, "expectations")

    transformed = transform(
        schema,
        data,
        options=options,
    )

    assert transformed == expectation


def test_path_not_found() -> None:
    schema = load(7, "cursors")
    data = load(3, "data")

    with raises(PathNotFound) as ex:
        transform(
            schema,
            data,
        )

    expect = (
        "Path \"fire_starters\" not found in record {'chefs': [{'name': "
        "'Alice'}, {'name': 'Bob'}, {'name': 'Charlie'}], 'firefighters': "
        "[{'name': 'Daniel'}, {'name': 'Esther'}, {'name': 'Freddy'}], "
        "'zookeepers': [{'name': 'Gregory'}, {'name': 'Harold'}, {'name': "
        "'Ingrid'}]}"
    )

    assert str(ex.value) == expect
