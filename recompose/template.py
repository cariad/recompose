from __future__ import annotations

from typing import Any

from recompose.cursor import Cursor
from recompose.cursors import find_cursor
from recompose.exceptions import (
    InvalidTemplatePropertyType,
    MissingTemplateProperty,
    UnsupportedTemplateVersion,
)
from recompose.logging import log
from recompose.types import TemplateType


class Template:
    """
    Recomposition template.
    """

    def __init__(
        self,
        cursor: Cursor,
        version: int,
    ) -> None:
        if version < 1 or version > 1:
            raise UnsupportedTemplateVersion(version, 1)

        self._cursor = cursor
        self._version = version

    @staticmethod
    def get_required_int(template: TemplateType, key: str) -> int:
        if value := template.get(key):
            if isinstance(value, int):
                return value

            raise InvalidTemplatePropertyType(key, int, value)

        raise MissingTemplateProperty(key, template)

    @classmethod
    def load(cls, template: TemplateType) -> Template:
        log.debug("Loading template: %s", template)

        version = cls.get_required_int(template, "version")
        cursor = find_cursor(template)

        return Template(
            cursor,
            version,
        )

    def transform(self, data: Any) -> Any:
        """
        Transforms and returns the data.
        """

        return self._cursor.transform(data)
