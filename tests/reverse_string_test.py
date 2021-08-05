from src.reverse_string import reverse


class TestReverseString:
    def test_an_empty_string(self) -> None:
        assert reverse("") == ""

    def test_a_word(self) -> None:
        assert reverse("robot") == "tobor"

    def test_a_capitalized_word(self) -> None:
        assert reverse("Ramen") == "nemaR"

    def test_a_sentence_with_punctuation(self) -> None:
        assert reverse("I'm hungry!") == "!yrgnuh m'I"

    def test_a_palindrome(self) -> None:
        assert reverse("racecar") == "racecar"

    def test_an_even_sized_word(self) -> None:
        assert reverse("drawer") == "reward"
