from recompose.exceptions.invalid_template import InvalidTemplate


class UnsupportedTemplateVersion(InvalidTemplate):
    """
    Raised when a template has an unsupported version.
    """

    def __init__(self, found: int, expected: int) -> None:
        super().__init__(
            "Found version %i but expected no later than %i"
            % (
                found,
                expected,
            )
        )
