def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    result: list[str] = []
    for cand in candidates:
        if word.lower() == cand.lower():
            continue
        elif sorted(word.lower()) == sorted(cand.lower()):
            result.append(cand)
    return result
