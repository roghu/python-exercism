from src.isogram import is_isogram


class TestIsogram:
    def test_empty_string(self) -> None:
        assert is_isogram("")

    def test_isogram_with_only_lower_case_characters(self) -> None:
        assert is_isogram("isogram")

    def test_word_with_one_duplicated_character(self) -> None:
        assert not is_isogram("eleven")

    def test_word_with_one_duplicated_character_from_the_end_of_the_alphabet(
        self,
    ) -> None:
        assert not is_isogram("zzyzx")

    def test_longest_reported_english_isogram(self) -> None:
        assert is_isogram("subdermatoglyphic")

    def test_word_with_duplicated_character_in_mixed_case(self) -> None:
        assert not is_isogram("Alphabet")

    def test_word_with_duplicated_character_in_mixed_case_lowercase_first(self) -> None:
        assert not is_isogram("alphAbet")

    def test_hypothetical_isogrammic_word_with_hyphen(self) -> None:
        assert is_isogram("thumbscrew-japingly")

    def test_hypothetical_word_with_duplicated_character_following_hyphen(self) -> None:
        assert not is_isogram("thumbscrew-jappingly")

    def test_isogram_with_duplicated_hyphen(self) -> None:
        assert is_isogram("six-year-old")

    def test_made_up_name_that_is_an_isogram(self) -> None:
        assert is_isogram("Emily Jung Schwartzkopf")

    def test_duplicated_character_in_the_middle(self) -> None:
        assert not is_isogram("accentor")

    def test_same_first_and_last_characters(self) -> None:
        assert not is_isogram("angola")
