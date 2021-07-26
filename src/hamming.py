def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("`strand_a` and `strand_b` are NOT the same length.")
    result = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            result += 1
    return result
