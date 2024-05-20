"""Main package for Cookiecutter."""

from pathlib import Path


def _get_version() -> str:
    """Read VERSION.txt and return its contents."""
    return "2.6.0"


__version__ = _get_version()
