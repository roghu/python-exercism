from string import ascii_lowercase, ascii_uppercase


def rotate(text: str, key: int) -> str:
    result = ""
    for letter in text:
        if letter in ascii_lowercase:
            idx = ascii_lowercase.index(letter)
            n = (idx + key) % 26
            result += ascii_lowercase[n]
        elif letter in ascii_uppercase:
            idx = ascii_uppercase.index(letter)
            n = (idx + key) % 26
            result += ascii_uppercase[n]
        else:
            result += letter
    return result
