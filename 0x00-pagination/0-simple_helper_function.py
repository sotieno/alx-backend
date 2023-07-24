#!/usr/bin/env python3
"""
    A helper function index_range
    Takes two int arguments (page, page_size)
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Return a tuple of size two containing a start index and an end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
