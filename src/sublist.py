from enum import Enum, auto
from typing import Any


class Category(Enum):
    SUBLIST = auto()
    SUPERLIST = auto()
    EQUAL = auto()
    UNEQUAL = auto()


def is_in_list(list_one: list[Any], list_two: list[Any]) -> bool:
    """Is `list_one` inside of `list_two`?"""
    if len(list_one) > len(list_two):
        return False
    list_one_len = len(list_one)
    for i in range(0, len(list_two) - list_one_len + 1):
        if list_one == list_two[i : i + list_one_len]:
            return True
    return False


def sublist(list_one: list[Any], list_two: list[Any]) -> Category:
    if list_one == list_two:
        return Category.EQUAL
    elif is_in_list(list_one, list_two):
        return Category.SUBLIST
    elif is_in_list(list_two, list_one):
        return Category.SUPERLIST
    return Category.UNEQUAL
