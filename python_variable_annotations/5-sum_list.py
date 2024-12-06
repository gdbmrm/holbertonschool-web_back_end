#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""

from typing import List

"""
Write a type-annotated function
sum_list which takes a list input_list
of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """
    function sum_list
    """
    somme = 0
    for element in input_list:
        somme += element
    return somme
