"""
Abstract class for reporter
"""
from abc import ABC, abstractmethod
from typing import Optional


class AbstractReporter(ABC):
    def __self__(
        self, base_url: str, token: Optional[str],
    ):
        self.base_url = base_url
        self.token = token

    @abstractmethod
    def report(self, url: str, **kwargs):
        raise NotImplementedError
