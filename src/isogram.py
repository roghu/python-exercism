import re


def is_isogram(string: str) -> bool:
    string = string.lower()
    string = re.sub(r"\W+", "", string)
    return len(set(string)) == len(string)
