from typing import List, Type

from recompose.cursor import Cursor
from recompose.cursors.each_value import EachValue
from recompose.cursors.this_value import ThisValue
from recompose.exceptions import NoCursorAvailable
from recompose.types import TemplateType

types: List[Type[Cursor]] = [
    EachValue,
    ThisValue,
]


def find_cursor(template: TemplateType) -> Cursor:
    """
    Finds and returns the first cursor that can handle a template.
    """

    for t in types:
        if t.key() in template:
            return t(template)

    raise NoCursorAvailable(template)


__all__ = [
    "find_cursor",
]
