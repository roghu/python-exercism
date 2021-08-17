import pytest

from src.largest_series_product import largest_product


class TestLargestSeriesProduct:
    def test_finds_the_largest_product_if_span_equals_length(self) -> None:
        assert largest_product("29", 2) == 18

    def test_can_find_the_largest_product_of_2_with_numbers_in_order(self) -> None:
        assert largest_product("0123456789", 2) == 72

    def test_can_find_the_largest_product_of_2(self) -> None:
        assert largest_product("576802143", 2) == 48

    def test_can_find_the_largest_product_of_3_with_numbers_in_order(self) -> None:
        assert largest_product("0123456789", 3) == 504

    def test_can_find_the_largest_product_of_3(self) -> None:
        assert largest_product("1027839564", 3) == 270

    def test_can_find_the_largest_product_of_5_with_numbers_in_order(self) -> None:
        assert largest_product("0123456789", 5) == 15120

    def test_can_get_the_largest_product_of_a_big_number(self) -> None:
        assert (
            largest_product("73167176531330624919225119674426574742355349194934", 6)
            == 23520
        )

    def test_reports_zero_if_the_only_digits_are_zero(self) -> None:
        assert largest_product("0000", 2) == 0

    def test_reports_zero_if_all_spans_include_zero(self) -> None:
        assert largest_product("99099", 3) == 0

    def test_rejects_span_longer_than_string_length(self) -> None:
        with pytest.raises(ValueError):
            largest_product("123", 4)

    def test_reports_1_for_empty_string_and_empty_product_0_span(self) -> None:
        assert largest_product("", 0) == 1

    def test_reports_1_for_nonempty_string_and_empty_product_0_span(self) -> None:
        assert largest_product("123", 0) == 1

    def test_rejects_empty_string_and_nonzero_span(self) -> None:
        with pytest.raises(ValueError):
            largest_product("", 1)

    def test_rejects_invalid_character_in_digits(self) -> None:
        with pytest.raises(ValueError):
            largest_product("1234a5", 2)

    def test_rejects_negative_span(self) -> None:
        with pytest.raises(ValueError):
            largest_product("12345", -1)

    def test_euler_big_number(self) -> None:
        assert (
            largest_product(
                "731671765313306249192251196744265747423553491949349698352031"
                "27745063262395783180169848018694788518438586156078911294949545950173"
                "795833195285320880551112540698747158523863050715693290963295227443043"
                "557668966489504452445231617318564030987111217223831136222989342338030"
                "813533627661428280644448664523874930358907296290491560440772390713810"
                "5158593079608667017242712188399879790879227492190169972088809377665727"
                "3330010533678812202354218097512545405947522435258490771167055601360483"
                "958644670632441572215539753697817977846174064955149290862569321978468"
                "622482839722413756570560574902614079729686524145351004748216637048440"
                "319989000889524345065854122758866688116427171479924442928230863465674"
                "813919123162824586178664583591245665294765456828489128831426076900422"
                "421902267105562632111110937054421750694165896040807198403850962455444"
                "3629812309878799272442849091888458015616609791913387549920052406368991"
                "256071760605886116467109405077541002256983155200055935729725716362695"
                "61882670428252483600823257530420752963450",
                13,
            )
            == 23514624000
        )
