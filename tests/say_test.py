import pytest

from src.say import say


class TestSay:
    def test_zero(self) -> None:
        assert say(0) == "zero"

    def test_one(self) -> None:
        assert say(1) == "one"

    def test_fourteen(self) -> None:
        assert say(14) == "fourteen"

    def test_twenty(self) -> None:
        assert say(20) == "twenty"

    def test_twenty_two(self) -> None:
        assert say(22) == "twenty-two"

    def test_one_hundred(self) -> None:
        assert say(100) == "one hundred"

    def test_one_hundred_twenty_three(self) -> None:
        assert say(123) == "one hundred twenty-three"

    def test_one_thousand(self) -> None:
        assert say(1000) == "one thousand"

    def test_one_thousand_two_hundred_thirty_four(self) -> None:
        assert say(1234) == "one thousand two hundred thirty-four"

    def test_one_million(self) -> None:
        assert say(1000000) == "one million"

    def test_one_million_two_thousand_three_hundred_forty_five(self) -> None:
        assert say(1002345) == "one million two thousand three hundred forty-five"

    def test_one_billion(self) -> None:
        assert say(1000000000) == "one billion"

    def test_a_big_number(self) -> None:
        assert (
            say(987654321123) == "nine hundred eighty-seven billion "
            "six hundred fifty-four million "
            "three hundred twenty-one thousand one hundred twenty-three"
        )

    def test_numbers_below_zero_are_out_of_range(self) -> None:
        with pytest.raises(ValueError):
            say(-1)

    def test_numbers_above_999_999_999_999_are_out_of_range(self) -> None:
        with pytest.raises(ValueError):
            say(1000000000000)

    def test_one_hundred_seventy(self) -> None:
        assert say(170) == "one hundred seventy"
