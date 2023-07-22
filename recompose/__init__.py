"""
Recompose is a Python package for templated data recomposition.
"""

from importlib.resources import open_text

from recompose.cursors import find_cursor
from recompose.exceptions import (
    InvalidTemplate,
    InvalidTemplatePropertyType,
    MissingTemplateProperty,
    NoCursorAvailable,
    NotATransformerType,
    RecomposeError,
    UnsupportedTemplateVersion,
)
from recompose.template import Template
from recompose.transformers import find_transformer

with open_text(__package__, "VERSION") as t:
    __version__ = t.readline().strip()


__all__ = [
    "InvalidTemplate",
    "InvalidTemplatePropertyType",
    "MissingTemplateProperty",
    "NoCursorAvailable",
    "NotATransformerType",
    "RecomposeError",
    "Template",
    "UnsupportedTemplateVersion",
    "find_cursor",
    "find_transformer",
]
