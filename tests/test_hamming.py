import pytest

from src.hamming import distance


class TestHamming:
    def test_empty_strands(self) -> None:
        assert distance("", "") == 0

    def test_single_letter_identical_strands(self) -> None:
        assert distance("A", "A") == 0

    def test_single_letter_different_strands(self) -> None:
        assert distance("G", "T") == 1

    def test_long_identical_strands(self) -> None:
        assert distance("GGACTGAAATCTG", "GGACTGAAATCTG") == 0

    def test_long_different_strands(self) -> None:
        assert distance("GGACGGATTCTG", "AGGACGGATTCT") == 9

    def test_disallow_first_strand_longer(self) -> None:
        with pytest.raises(ValueError):
            distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self) -> None:
        with pytest.raises(ValueError):
            distance("ATA", "AGTG")

    def test_disallow_left_empty_strand(self) -> None:
        with pytest.raises(ValueError):
            distance("", "G")

    def test_disallow_right_empty_strand(self) -> None:
        with pytest.raises(ValueError):
            distance("G", "")
