from recompose.cursor import Cursor


class ThisValue(Cursor):
    """
    A cursor that expects and yields a single value.
    """

    @classmethod
    def key(cls) -> str:
        """
        Key.
        """

        return "this-value"
