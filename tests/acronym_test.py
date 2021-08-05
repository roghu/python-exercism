from src.acronym import abbreviate


class TestAcronym:
    def test_basic(self) -> None:
        assert abbreviate("Portable Network Graphics") == "PNG"

    def test_lowercase_words(self) -> None:
        assert abbreviate("Ruby on Rails") == "ROR"

    def test_punctuation(self) -> None:
        assert abbreviate("First In, First Out") == "FIFO"

    def test_all_caps_word(self) -> None:
        assert abbreviate("GNU Image Manipulation Program") == "GIMP"

    def test_punctuation_without_whitespace(self) -> None:
        assert abbreviate("Complementary metal-oxide semiconductor") == "CMOS"

    def test_very_long_abbreviation(self) -> None:
        expected = (
            "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"
        )
        assert abbreviate(expected) == "ROTFLSHTMDCOALM"

    def test_consecutive_delimiters(self) -> None:
        assert abbreviate("Something - I made up from thin air") == "SIMUFTA"

    def test_apostrophes(self) -> None:
        assert abbreviate("Halley's Comet") == "HC"

    def test_underscore_emphasis(self) -> None:
        assert abbreviate("The Road _Not_ Taken") == "TRNT"
