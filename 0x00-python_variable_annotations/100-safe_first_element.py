#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Iterable, Sequence, List, Tuple, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe first element """
    if lst:
        return lst[0]
    else:
        return None
