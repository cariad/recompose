from recompose.exceptions.invalid_template import InvalidTemplate
from recompose.types import TransformerType


class NotATransformerType(InvalidTemplate):
    """
    Raised when a query does not match any transformer types.
    """

    def __init__(self, transformer_type: TransformerType) -> None:
        super().__init__("%s is not a known transformer" % transformer_type)
