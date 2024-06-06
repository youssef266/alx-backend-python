#!/usr/bin/env python3
""" 
Write a type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns:the sum of the float in the list"""
    return float(sum(input_list))
