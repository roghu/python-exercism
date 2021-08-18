from src.roman_numerals import roman


class TestRomanNumerals:
    def test_1_is_i(self) -> None:
        assert roman(1) == "I"

    def test_2_is_ii(self) -> None:
        assert roman(2) == "II"

    def test_3_is_iii(self) -> None:
        assert roman(3) == "III"

    def test_4_is_iv(self) -> None:
        assert roman(4) == "IV"

    def test_5_is_v(self) -> None:
        assert roman(5) == "V"

    def test_6_is_vi(self) -> None:
        assert roman(6) == "VI"

    def test_9_is_ix(self) -> None:
        assert roman(9) == "IX"

    def test_27_is_xxvii(self) -> None:
        assert roman(27) == "XXVII"

    def test_48_is_xlviii(self) -> None:
        assert roman(48) == "XLVIII"

    def test_49_is_xlix(self) -> None:
        assert roman(49) == "XLIX"

    def test_59_is_lix(self) -> None:
        assert roman(59) == "LIX"

    def test_93_is_xciii(self) -> None:
        assert roman(93) == "XCIII"

    def test_141_is_cxli(self) -> None:
        assert roman(141) == "CXLI"

    def test_163_is_clxiii(self) -> None:
        assert roman(163) == "CLXIII"

    def test_402_is_cdii(self) -> None:
        assert roman(402) == "CDII"

    def test_575_is_dlxxv(self) -> None:
        assert roman(575) == "DLXXV"

    def test_911_is_cmxi(self) -> None:
        assert roman(911) == "CMXI"

    def test_1024_is_mxxiv(self) -> None:
        assert roman(1024) == "MXXIV"

    def test_3000_is_mmm(self) -> None:
        assert roman(3000) == "MMM"
