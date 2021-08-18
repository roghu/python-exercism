def factors(value: int) -> list[int]:
    result: list[int] = []
    i = 2
    while i * i <= value:
        while value % i == 0:
            result.append(i)
            value //= i
        i += 1
    if value > 1:
        result.append(value)
    return result
