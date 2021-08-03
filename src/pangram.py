import re


def is_pangram(sentence: str) -> bool:
    if not sentence:
        return False
    sentence = re.sub(r"[\W\d_]", "", sentence)
    return len(set(sentence.lower())) == 26
