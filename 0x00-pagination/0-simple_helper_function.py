#!/usr/bin/env python3
"""
Main file
"""


def index_range(page: int, page_size: int):
    StartIndex = (page - 1) * page_size
    EndIndex = StartIndex + page_size
    return (StartIndex, EndIndex)
