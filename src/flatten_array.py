from typing import Any


def flatten(iterable: list[Any]) -> list[Any]:
    result: list[int] = []
    for i in iterable:
        if isinstance(i, list):
            result.extend(flatten(i))
        elif i is not None:
            result.append(i)
    return result
