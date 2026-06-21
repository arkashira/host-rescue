"""
axentx_product
==============

A tiny utility package used by the AxentX product pipeline.

Public API
----------

- `reverse_string(text: str) -> str`
    Returns the input string reversed.  It raises a `TypeError` if the
    argument is not a string.

The implementation is deliberately simple and has full test coverage.
"""

from __future__ import annotations

__all__ = ["reverse_string"]


def reverse_string(text: str) -> str:
    """
    Return a new string containing the characters of *text* in reverse order.

    Parameters
    ----------
    text: str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.

    Raises
    ------
    TypeError
        If *text* is not an instance of `str`.

    Examples
    --------
    >>> reverse_string("abc")
    'cba'
    >>> reverse_string("")
    ''
    """
    if not isinstance(text, str):
        raise TypeError(f"reverse_string expects a str, got {type(text)!r}")
    # Slicing is the most idiomatic and efficient way to reverse a string.
    return text[::-1]
