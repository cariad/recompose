from pathlib import Path
from typing import Any
from unittest.mock import Mock

from pytest import mark, raises
from yaml import safe_load

from recompose import (
    InvalidTemplatePropertyType,
    MissingTemplateProperty,
    Template,
    UnsupportedTemplateVersion,
)

tests = Path() / "tests"


def load(id: int, dir: str) -> Any:
    padded_id = str(id).rjust(3, "0")
    path = tests / dir / f"{padded_id}.yml"

    with open(path, "r") as f:
        return safe_load(f)


@mark.parametrize(
    "template_id, data_id, expectation_id",
    [
        (0, 0, 0),
        (1, 0, 0),
        (2, 0, 0),
    ],
)
def test_transform(template_id: int, data_id: int, expectation_id: int) -> None:
    template = Template.load(load(template_id, "templates"))
    data = load(data_id, "data")
    expectation = load(expectation_id, "expectations")
    transformed = template.transform(data)
    assert transformed == expectation


def test_version__none() -> None:
    with raises(MissingTemplateProperty) as ex:
        Template.load({})

    assert str(ex.value) == "Required template key version is not present ({})"


def test_version__not_integer() -> None:
    with raises(InvalidTemplatePropertyType) as ex:
        Template.load({"version": "foo"})

    expect = "Expected template key version to be int but found foo (str)"

    assert str(ex.value) == expect


def test_version__unsupported() -> None:
    with raises(UnsupportedTemplateVersion) as ex:
        Template(Mock(), 999)

    assert str(ex.value) == "Found version 999 but expected no later than 1"
