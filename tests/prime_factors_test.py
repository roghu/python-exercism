from src.prime_factors import factors


class TestPrimeFactors:
    def test_no_factors(self) -> None:
        assert factors(1) == []

    def test_prime_number(self) -> None:
        assert factors(2) == [2]

    def test_square_of_a_prime(self) -> None:
        assert factors(9) == [3, 3]

    def test_cube_of_a_prime(self) -> None:
        assert factors(8) == [2, 2, 2]

    def test_product_of_primes_and_non_primes(self) -> None:
        assert factors(12) == [2, 2, 3]

    def test_product_of_primes(self) -> None:
        assert factors(901255) == [5, 17, 23, 461]

    def test_factors_include_a_large_prime(self) -> None:
        assert factors(93819012551) == [11, 9539, 894119]
