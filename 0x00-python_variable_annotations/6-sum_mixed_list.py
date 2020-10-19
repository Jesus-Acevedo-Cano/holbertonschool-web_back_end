#!/usr/bin/env python3
""" Complex types - mixed list  """
from typing import List


def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """ type-annotated function """
    return float(sum(mxd_lst))
