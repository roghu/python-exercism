def is_mulitple(number: int, multiple: int) -> bool:
    return multiple != 0 and number % multiple == 0


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    nums: set[int] = set()
    for i in range(1, limit):
        for multiple in multiples:
            if is_mulitple(i, multiple):
                nums.add(i)
    return sum(nums)
