def slices(series: str, length: int) -> list[str]:
    if not series or length > 5 or length < 1:
        raise ValueError
    return [series[i : length + i] for i in range(0, len(series) - length + 1)]
