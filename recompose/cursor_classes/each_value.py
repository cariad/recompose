from typing import Any, List

from recompose.cursor import Cursor
from recompose.logging import log


class EachValue(Cursor):
    """
    A cursor that expects and yields each value in a list or dictionary.
    """

    def _transform(self, data: Any) -> Any:
        result: List[Any] = []

        for child in data:
            log.debug("%s transforming child item %s", self, child)

            for transformer in self.transformers:
                transformed = transformer.transform(child)

                log.debug(
                    "%s transformed child item %s to %s",
                    self,
                    child,
                    transformed,
                )

                result.append(transformed)

        return result

    @classmethod
    def condition(cls) -> str:
        return "each-value"
