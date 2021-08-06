from src.luhn import Luhn


class TestLuhn:
    def test_single_digit_strings_can_not_be_valid(self) -> None:
        assert not Luhn("1").valid()

    def test_a_single_zero_is_invalid(self) -> None:
        assert not Luhn("0").valid()

    def test_a_simple_valid_sin_that_remains_valid_if_reversed(self) -> None:
        assert Luhn("059").valid()

    def test_a_simple_valid_sin_that_becomes_invalid_if_reversed(self) -> None:
        assert Luhn("59").valid()

    def test_a_valid_canadian_sin(self) -> None:
        assert Luhn("055 444 285").valid()

    def test_invalid_canadian_sin(self) -> None:
        assert not Luhn("055 444 286").valid()

    def test_invalid_credit_card(self) -> None:
        assert not Luhn("8273 1232 7352 0569").valid()

    def test_invalid_long_number_with_an_even_remainder(self) -> None:
        assert not Luhn("1 2345 6789 1234 5678 9012").valid()

    def test_valid_number_with_an_even_number_of_digits(self) -> None:
        assert Luhn("095 245 88").valid()

    def test_valid_number_with_an_odd_number_of_spaces(self) -> None:
        assert Luhn("234 567 891 234").valid()

    def test_valid_strings_with_a_non_digit_added_at_the_end_become_invalid(
        self,
    ) -> None:
        assert not Luhn("059a").valid()

    def test_valid_strings_with_punctuation_included_become_invalid(self) -> None:
        assert not Luhn("055-444-285").valid()

    def test_valid_strings_with_symbols_included_become_invalid(self) -> None:
        assert not Luhn("055# 444$ 285").valid()

    def test_single_zero_with_space_is_invalid(self) -> None:
        assert not Luhn(" 0").valid()

    def test_more_than_a_single_zero_is_valid(self) -> None:
        assert Luhn("0000 0").valid()

    def test_input_digit_9_is_correctly_converted_to_output_digit_9(self) -> None:
        assert Luhn("091").valid()

    def test_using_ascii_value_for_non_doubled_non_digit_isn_t_allowed(self) -> None:
        assert not Luhn("055b 444 285").valid()

    def test_using_ascii_value_for_doubled_non_digit_isn_t_allowed(self) -> None:
        assert not Luhn(":9").valid()

    def test_is_valid_can_be_called_repeatedly(self) -> None:
        # This test was added, because we saw many implementations
        # in which the first call to valid() worked, but the
        # second call failed().
        number = Luhn("055 444 285")
        assert number.valid()
        assert number.valid()
