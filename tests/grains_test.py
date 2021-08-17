import pytest

from src.grains import square, total


class TestGrains:
    def test_grains_on_square_1(self) -> None:
        assert square(1) == 1

    def test_grains_on_square_2(self) -> None:
        assert square(2) == 2

    def test_grains_on_square_3(self) -> None:
        assert square(3) == 4

    def test_grains_on_square_4(self) -> None:
        assert square(4) == 8

    def test_grains_on_square_16(self) -> None:
        assert square(16) == 32768

    def test_grains_on_square_32(self) -> None:
        assert square(32) == 2147483648

    def test_grains_on_square_64(self) -> None:
        assert square(64) == 9223372036854775808

    def test_square_0_raises_an_exception(self) -> None:
        with pytest.raises(ValueError):
            square(0)

    def test_negative_square_raises_an_exception(self) -> None:
        with pytest.raises(ValueError):
            square(-1)

    def test_square_greater_than_64_raises_an_exception(self) -> None:
        with pytest.raises(ValueError):
            square(65)

    def test_returns_the_total_number_of_grains_on_the_board(self) -> None:
        assert total() == 18446744073709551615
