from typing import NamedTuple


Counter = NamedTuple("Counter", (("letter", str), ("count", int)))


def _count_encoding(string: str) -> list[Counter]:
    result: list[Counter] = []
    tmp = ""
    count = 1
    for letter in string:
        if letter.isdigit():
            tmp += letter
        else:
            if tmp.isdigit():
                count = int(tmp)
                tmp = ""

            result.append(Counter(letter, count))
            count = 1

    return result


def _create_msg(counters: list[Counter]) -> str:
    return "".join(c.letter * c.count for c in counters)


def decode(string: str) -> str:
    counters = _count_encoding(string)
    result = _create_msg(counters)
    return result


def _count_letters(string: str) -> list[Counter]:
    result: list[Counter] = []
    last_letter = ""
    count = 1
    for letter in string:
        if last_letter == letter:
            count += 1
        else:
            if last_letter != "":
                result.append(Counter(last_letter, count))
            count = 1
            last_letter = letter
    result.append(Counter(last_letter, count))
    return result


def _create_encoding(counters: list[Counter]) -> str:
    return "".join(f"{c.count if c.count > 1 else ''}{c.letter}" for c in counters)


def encode(string: str) -> str:
    result = ""
    counts = _count_letters(string)
    result = _create_encoding(counts)
    return result
