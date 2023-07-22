from recompose.exceptions.recompose import RecomposeError


class InvalidTemplate(RecomposeError):
    """
    Raised when a template is invalid.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
