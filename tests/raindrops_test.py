from src.raindrops import convert


class TestRaindrops:
    def test_the_sound_for_1_is_1(self) -> None:
        assert convert(1) == "1"

    def test_the_sound_for_3_is_pling(self) -> None:
        assert convert(3) == "Pling"

    def test_the_sound_for_5_is_plang(self) -> None:
        assert convert(5) == "Plang"

    def test_the_sound_for_7_is_plong(self) -> None:
        assert convert(7) == "Plong"

    def test_the_sound_for_6_is_pling_as_it_has_a_factor_3(self) -> None:
        assert convert(6) == "Pling"

    def test_2_to_the_power_3_doesnt_make_raindrop_sound_as_3_is_the_exp_not_the_base(
        self,
    ) -> None:
        assert convert(8) == "8"

    def test_the_sound_for_9_is_pling_as_it_has_a_factor_3(self) -> None:
        assert convert(9) == "Pling"

    def test_the_sound_for_10_is_plang_as_it_has_a_factor_5(self) -> None:
        assert convert(10) == "Plang"

    def test_the_sound_for_14_is_plong_as_it_has_a_factor_of_7(self) -> None:
        assert convert(14) == "Plong"

    def test_the_sound_for_15_is_pling_plang_as_it_has_factors_3_and_5(self) -> None:
        assert convert(15) == "PlingPlang"

    def test_the_sound_for_21_is_pling_plong_as_it_has_factors_3_and_7(self) -> None:
        assert convert(21) == "PlingPlong"

    def test_the_sound_for_25_is_plang_as_it_has_a_factor_5(self) -> None:
        assert convert(25) == "Plang"

    def test_the_sound_for_27_is_pling_as_it_has_a_factor_3(self) -> None:
        assert convert(27) == "Pling"

    def test_the_sound_for_35_is_plang_plong_as_it_has_factors_5_and_7(self) -> None:
        assert convert(35) == "PlangPlong"

    def test_the_sound_for_49_is_plong_as_it_has_a_factor_7(self) -> None:
        assert convert(49) == "Plong"

    def test_the_sound_for_52_is_52(self) -> None:
        assert convert(52) == "52"

    def test_the_sound_for_105_is_pling_plang_plong_as_it_has_factors_3_5_and_7(
        self,
    ) -> None:
        assert convert(105) == "PlingPlangPlong"

    def test_the_sound_for_3125_is_plang_as_it_has_a_factor_5(self) -> None:
        assert convert(3125) == "Plang"
