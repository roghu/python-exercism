VOWELS = ("a", "e", "i", "o", "u", "xr", "yt")


def translate(text: str) -> str:
    result: list[str] = []
    for word in text.split():
        if word.startswith(VOWELS):
            begin, end = "", word
        elif word.startswith("qu"):
            begin, end = word[:2], word[2:]
        elif word.startswith("squ"):
            begin, end = word[:3], word[3:]
        else:
            for i, letter in enumerate(word):
                if letter in ["a", "e", "i", "o", "u"]:
                    break
                elif i != 0 and letter == "y":
                    break
            begin, end = word[:i], word[i:]
        result.append(f"{end}{begin}ay")
    return " ".join(result)
