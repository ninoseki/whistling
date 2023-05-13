"""
Abstract class for reporter
"""
from abc import ABC, abstractmethod


class AbstractReporter(ABC):
    def __self__(self, token: str | None = None, *, base_url: str):
        self.base_url = base_url
        self.token = token

    @abstractmethod
    def report(self, url: str, **kwargs):
        raise NotImplementedError
