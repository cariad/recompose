from pathlib import Path
from typing import Any

from pytest import mark
from ruamel.yaml import YAML

from recompose import make_cursor

test_data = Path() / "tests" / "data"
yaml = YAML(typ="safe")


def load(id: int, dir: str) -> Any:
    padded_id = str(id).rjust(3, "0")
    path = test_data / dir / f"{padded_id}.yml"

    with open(path, "r") as f:
        return yaml.load(f)


@mark.parametrize(
    "cursor_id, data_id, expectation_id",
    [
        (0, 0, 0),
        (1, 1, 1),
        (2, 2, 2),
    ],
)
def test(cursor_id: int, data_id: int, expectation_id: int) -> None:
    cursor_definition = load(cursor_id, "cursors")
    cursor = make_cursor(cursor_definition)
    data = load(data_id, "data")
    expectation = load(expectation_id, "expectations")
    transformed = cursor.transform(data)
    assert transformed == expectation
