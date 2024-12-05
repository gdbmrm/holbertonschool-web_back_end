#!/usr/bin/env python3

"""
9. Let's duck type an iterable object
"""

from typing import Sequence, Iterable, List

"""
Annotate the below function’s parameters and return values with the appropriate types
"""

def element_length(lst: Iterable[Sequence]) -> list[Sequence, int] :
    """
    function element_length
    """
    return [(i, len(i)) for i in lst]