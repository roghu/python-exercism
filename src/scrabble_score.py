def score_value(value: int, letters: str) -> dict[str, int]:
    return {letter: value for letter in letters}


SCORE = score_value(1, "a e i o u l n r s t")
SCORE.update(score_value(2, "d g"))
SCORE.update(score_value(3, "b c m p"))
SCORE.update(score_value(4, "f h v w y"))
SCORE.update(score_value(5, "k"))
SCORE.update(score_value(8, "j x"))
SCORE.update(score_value(10, "q z"))


def score(word: str) -> int:
    return sum(SCORE[letter] for letter in word.lower())
