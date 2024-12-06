#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""

from typing import Union, List

"""
Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list
    """
    somme = 0
    for element in mxd_lst:
        somme += element
    return somme
