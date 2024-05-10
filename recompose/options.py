class Options:
    """
    Recomposition options.

    `allow_missing_data` describes whether missing data should be accepted or
    raise `PathNotFound`.
    """

    def __init__(
        self,
        allow_missing_data: bool = False,
    ) -> None:
        self.allow_missing_data = allow_missing_data
