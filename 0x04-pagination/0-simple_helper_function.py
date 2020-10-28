#!/usr/bin/env python3
""" Simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ return start index and end index """
    start: int = (page -1) * page_size
    end: int = page_size * page
    return (start, end)
