from abc import ABC, abstractmethod
from typing import Any, Iterable, cast

from recompose.logging import log
from recompose.transformer import Transformer
from recompose.transformers import find_transformer
from recompose.types import TemplateType, TransformerTypes


class Cursor(ABC):
    """
    Transformer cursor.
    """

    def __init__(self, template: TemplateType) -> None:
        self._template = template

    def __str__(self) -> str:
        return self.key()

    @abstractmethod
    def _transform(self, data: Any) -> Any:
        """
        Transforms and returns the data.
        """

    @classmethod
    @abstractmethod
    def key(cls) -> str:
        """
        Key.
        """

    def transform(self, data: Any) -> Any:
        """
        Transforms and returns the data.
        """

        log.debug("%s started transforming %s", self, data)
        return self._transform(data)

    @property
    def transformers(self) -> Iterable[Transformer]:
        """
        Yields each transformer.
        """

        value = self._template[self.key()]
        value = cast(TransformerTypes, value)

        if isinstance(value, list):
            for t in value:
                yield find_transformer(t)
        else:
            yield find_transformer(value)
