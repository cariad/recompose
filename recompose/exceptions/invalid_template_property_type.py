from typing import Any, Type

from recompose.exceptions.invalid_template import InvalidTemplate


class InvalidTemplatePropertyType(InvalidTemplate):
    """
    Raised when a template property is of the wrong type.
    """

    def __init__(self, key: str, expected: Type[Any], found: Any) -> None:
        super().__init__(
            "Expected template key %s to be %s but found %s (%s)"
            % (
                key,
                expected.__name__,
                found,
                found.__class__.__name__,
            )
        )
