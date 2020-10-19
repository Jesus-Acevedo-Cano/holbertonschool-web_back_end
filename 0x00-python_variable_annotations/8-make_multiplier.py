#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function """
    def multiply(a: float):
        """ function to multiply a float by multiplier """
        return a * multiplier
    return multiply
