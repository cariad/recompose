from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional

from recompose.logging import log
from recompose.types import WithArgs


class Transformer(ABC):
    """
    Abstract transformer.
    """

    def __init__(
        self,
        with_args: Optional[WithArgs] = None,
    ) -> None:
        self._with_args = with_args
        log.debug("Created %s with %s", self, with_args)

    def __str__(self) -> str:
        return self.name()

    @abstractmethod
    def _transform(self, data: Any) -> Any:
        """
        Transforms and returns the data.
        """

    @classmethod
    @abstractmethod
    def name(cls) -> str:
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
    def with_args(self) -> Optional[WithArgs]:
        """
        Transformation arguments.
        """

        return self._with_args
