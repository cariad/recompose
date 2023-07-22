from abc import ABC, abstractmethod
from typing import Any


class Transformer(ABC):
    """
    Abstract transformer.
    """

    def __str__(self) -> str:
        return self.key()

    @classmethod
    @abstractmethod
    def key(cls) -> str:
        """
        Key.
        """

    @abstractmethod
    def transform(self, data: Any) -> Any:
        """
        Transforms and returns the data.
        """
