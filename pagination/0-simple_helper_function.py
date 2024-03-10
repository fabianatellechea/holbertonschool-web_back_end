#!/usr/bin/env python3
"""function named index_range that takes
two integer arguments page and page_size"""


def index_range(page, page_size):
    """return a tuple of size two"""
    last_index = page * page_size
    first_index = last_index - page_size
    return (first_index, last_index)
