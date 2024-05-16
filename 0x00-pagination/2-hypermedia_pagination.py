#!/usr/bin/env python3
"""
get spicific page from a dataset
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate th start and the end index for pangination
    """
    StartIndex = (page - 1) * page_size
    EndIndex = StartIndex + page_size
    return (StartIndex, EndIndex)


class Server:
    """
    Server class to paginate a database of popular baby names.
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
        """
        Get the correct pages from the dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get Hypermedia pagination
        """
        data = self.get_page(page, page_size)
        size = len(data)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = None
        if page + 1 <= total_pages:
            next_page = page + 1
        prev_page = None
        if page > 1:
            prev_page = page - 1
        hypermedia = {
                'page_size': size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }

        return hypermedia
