def multiple(nums: list[int]) -> int:
    result = 1
    for x in nums:
        result *= x
    return result


def largest_product(series: str, size: int) -> int:
    if size > len(series) or size < 0:
        raise ValueError
    products: list[int] = []
    int_series = [int(x) for x in series]
    has_zero = True
    for i in range(0, len(int_series) - size + 1):
        if has_zero and 0 not in int_series[i : i + size]:
            has_zero = False
        products.append(multiple(int_series[i : i + size]))
    return 0 if has_zero else max(products)
