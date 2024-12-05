#!/usr/bin/env python3

"""
8. Complex types - functions
"""

from typing import Callable

"""
Write a type-annotated function make_multiplier
that takes a float multiplier as argument and returns
a function that multiplies a float by multiplier.
"""

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
