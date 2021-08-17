import re
from string import ascii_lowercase
from typing import Iterator


def coding(text: str) -> list[str]:
    result: list[str] = []
    text = re.sub(r"[^a-zA-Z0-9]+", "", text)
    for letter in text.lower():
        if letter.isdigit():
            result.append(letter)
        else:
            i = ascii_lowercase.index(letter)
            result.append(ascii_lowercase[-i - 1])
    return result


def string_of_n(lst: list[str], n: int) -> Iterator[str]:
    for i in range(0, len(lst) // 2):
        yield "".join(lst[i * n : i * n + n])


def encode(plain_text: str) -> str:
    cipher = coding(plain_text)
    return " ".join(string_of_n(cipher, 5)).rstrip()


def decode(ciphered_text: str) -> str:
    return "".join(coding(ciphered_text))
