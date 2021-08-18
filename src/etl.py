def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    result: dict[str, int] = {}
    for k, v in legacy_data.items():
        for letter in v:
            result[letter.lower()] = k
    return result
