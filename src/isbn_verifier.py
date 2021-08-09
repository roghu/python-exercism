import re


def is_valid(isbn: str) -> bool:
    isbn = re.sub(r"[\-]+", "", isbn)
    if len(isbn) != 10:
        return False

    isbn_lst: list[int] = []
    for i, s in enumerate(isbn):
        if s == "X" and i == 9:
            isbn_lst.append(10)
        elif s.isdigit():
            isbn_lst.append(int(s))
        else:
            return False

    checksum = sum(n * m for n, m in zip(isbn_lst, list(range(10, 0, -1))))
    return checksum % 11 == 0
