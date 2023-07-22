from abc import ABC, abstractmethod
from typing import Iterable, cast

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

    @classmethod
    @abstractmethod
    def key(cls) -> str:
        """
        Key.
        """

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
