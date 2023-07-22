from recompose.exceptions.invalid_template import InvalidTemplate
from recompose.types import TemplateType


class NoCursorAvailable(InvalidTemplate):
    """
    Raised when there are no cursors available that support a given template.
    """

    def __init__(self, template: TemplateType) -> None:
        super().__init__("No cursors support this template (%s)" % template)
