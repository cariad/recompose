from typing import Any, List

from recompose.cursor import Cursor
from recompose.logging import log


class EachValue(Cursor):
    """
    A cursor that expects and yields each value in a list or dictionary.
    """

    def _transform(self, data: Any) -> Any:
        result: List[Any] = []

        for item in data:
            log.debug("%s transforming child item %s", self, item)

            for transformer in self.transformers:
                transformed = transformer.transform(item)

                log.debug(
                    "%s transformed child item %s to %s",
                    self,
                    item,
                    transformed,
                )

                result.append(transformed)

        return result

    @classmethod
    def key(cls) -> str:
        return "each-value"
