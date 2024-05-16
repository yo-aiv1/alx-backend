#!/usr/bin/env python3
"""
The helper funtion file
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate th start and the end index for pangination
    """
    StartIndex = (page - 1) * page_size
    EndIndex = StartIndex + page_size
    return (StartIndex, EndIndex)
