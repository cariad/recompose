from typing import List, Type

from recompose.exceptions import NotATransformerType
from recompose.transformer import Transformer
from recompose.transformers.list_to_object import ListToObject
from recompose.types import TransformerType

types: List[Type[Transformer]] = [
    ListToObject,
]


def find_transformer(transformer_type: TransformerType) -> Transformer:
    """
    Finds and returns the first transformer that fits a definition.
    """

    for t in types:
        if t.key() == transformer_type or t.key() in transformer_type:
            return t()

    raise NotATransformerType(transformer_type)


__all__ = [
    "find_transformer",
]
