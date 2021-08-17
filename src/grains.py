def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError
    result = 1
    for _ in range(1, number):
        result *= 2
    return result


def total() -> int:
    return sum(square(i) for i in range(1, 65))
