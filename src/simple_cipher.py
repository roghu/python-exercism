from itertools import cycle
from random import randint
from string import ascii_lowercase as lowercase
from typing import Optional


class Cipher:
    def __init__(self, key: Optional[str] = None) -> None:
        if not key:
            self.key = ""
            for _ in range(0, 101):
                self.key += lowercase[randint(0, 25)]
        else:
            self.key = key

    def encode(self, text: str) -> str:
        result: list[str] = []
        keys = cycle(self.key)
        for letter in text:
            idx = lowercase.index(letter)
            shift_idx = lowercase.index(next(keys))
            total = (idx + shift_idx) % 26
            result.append(lowercase[total])
        return "".join(result)

    def decode(self, text: str) -> str:
        result: list[str] = []
        keys = cycle(self.key)
        for letter in text:
            idx = lowercase.index(letter)
            shift_idx = lowercase.index(next(keys))
            total = (idx - shift_idx) % 26
            result.append(lowercase[total])
        return "".join(result)
