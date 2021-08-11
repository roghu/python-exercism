from src.rotational_cipher import rotate


class TestRotationalCipher:
    def test_rotate_a_by_0_same_output_as_input(self) -> None:
        assert rotate("a", 0) == "a"

    def test_rotate_a_by_1(self) -> None:
        assert rotate("a", 1) == "b"

    def test_rotate_a_by_26_same_output_as_input(self) -> None:
        assert rotate("a", 26) == "a"

    def test_rotate_m_by_13(self) -> None:
        assert rotate("m", 13) == "z"

    def test_rotate_n_by_13_with_wrap_around_alphabet(self) -> None:
        assert rotate("n", 13) == "a"

    def test_rotate_capital_letters(self) -> None:
        assert rotate("OMG", 5) == "TRL"

    def test_rotate_spaces(self) -> None:
        assert rotate("O M G", 5) == "T R L"

    def test_rotate_numbers(self) -> None:
        assert rotate("Testing 1 2 3 testing", 4) == "Xiwxmrk 1 2 3 xiwxmrk"

    def test_rotate_punctuation(self) -> None:
        assert rotate("Let's eat, Grandma!", 21) == "Gzo'n zvo, Bmviyhv!"

    def test_rotate_all_letters(self) -> None:
        assert (
            rotate("The quick brown fox jumps over the lazy dog.", 13)
            == "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
        )
