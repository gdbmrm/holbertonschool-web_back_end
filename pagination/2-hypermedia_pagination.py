#!/usr/bin/env python3
"""
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function index_range
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


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
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        self.__dataset = self.dataset()

        start, end = index_range(page, page_size)

        if end > len(self.__dataset) or start > len(self.__dataset):
            return []

        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        pages = self.get_page(page, page_size)
        next_pages = page + 1
        prev_pages = page - 1
        total_pages = round(len(self.__dataset) / page_size)

        if page > total_pages:
            next_pages = None

        if prev_pages <= 0:
            prev_pages = None

        my_dict = {
            "page_size": len(pages),
            "page": page,
            "data": pages,
            "next_page": next_pages,
            "prev_page": prev_pages,
            "total_pages": total_pages
        }

        return my_dict