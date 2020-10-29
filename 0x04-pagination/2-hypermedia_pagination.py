#!/usr/bin/env python3
""" Simple helper function """
import csv
import math
from typing import List, Dict, Union


def index_range(page: int, page_size: int) -> tuple:
    """ return start index and end index """
    start: int = (page - 1) * page_size
    end: int = page_size * page
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ method to get the correct page """
        dataset = self.dataset()
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        if end > len(dataset):
            return []
        return [(dataset[value]) for value in range(start, end)]

    def get_hyper(self, page: int = 1, page_size: int = 10) ->\
            Dict[str, Union[List[List], None, int]]:
        """ get hyper method """
        data: list = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)
        page_size: int = 0 if data == [] else page_size
        page: int = page
        next_page: int = None if page == len(self.dataset())\
            or data == [] else page + 1
        prev_page: int = None if page == 1 else page - 1
        return {'page_size': page_size, 'page': page,
                'data': data, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': total_pages}
