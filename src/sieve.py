def primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = [True for _ in range(2, limit + 1)]
    for n in range(2, limit + 1 // 2):
        for j in range(n + n - 2, limit - 1, n):
            sieve[j] = False
    return [n + 2 for n, b in enumerate(sieve) if b]
