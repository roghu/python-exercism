import re

delimters = re.compile(r"[-_\s]+")


def abbreviate(words: str) -> str:
    word_list = re.split(delimters, words)
    return "".join(word[0].upper() for word in word_list)
