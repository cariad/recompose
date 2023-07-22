from typing import Any

from recompose.transformer import Transformer


class ListToObject(Transformer):
    """
    Transforms a list into a single object.
    """

    @classmethod
    def key(cls) -> str:
        """
        Key.
        """

        return "list-to-object"

    def transform(self, data: Any) -> Any:
        """
        Transforms and returns the data.
        """

        return data[0]
