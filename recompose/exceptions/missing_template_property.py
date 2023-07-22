from recompose.exceptions.invalid_template import InvalidTemplate
from recompose.types import TemplateType


class MissingTemplateProperty(InvalidTemplate):
    """
    Raised when a required template property is not present.
    """

    def __init__(self, key: str, template: TemplateType) -> None:
        super().__init__(
            "Required template key %s is not present (%s)" % (key, template)
        )
