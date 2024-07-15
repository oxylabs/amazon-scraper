"""
    Module for base exception class.
"""


class BaseException(Exception):
    """Base exception class"""

    message: str = ""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or self.message)
