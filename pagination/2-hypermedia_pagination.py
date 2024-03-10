#!/usr/bin/env python3
"""function named index_range that takes
two integer arguments page and page_size"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple of size two"""
    last_index = page * page_size
    first_index = last_index - page_size
    return (first_index, last_index)


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
        """func that returns the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        range = index_range(page, page_size)
        data = self.dataset()
        return data[range[0]:range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Hypermedia pagination"""
        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if (page - 1) * page_size + len(dataset_page) < len(self.dataset()):
            next_page = page + 1
        else:
            next_page = None
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
