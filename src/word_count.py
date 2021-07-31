import re

words = re.compile(r"(\w+'\w|\w+)")


def count_words(sentence: str) -> dict[str, int]:
    result: dict[str, int] = {}
    sentence = re.sub(r"_", " ", sentence)
    for word in re.findall(words, sentence):
        word = word.lower()
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
