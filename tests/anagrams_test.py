from src.anagrams import find_anagrams


class TestAnagram:
    def test_no_matches(self) -> None:
        candidates = ["hello", "world", "zombies", "pants"]
        expected: list[str] = []
        assert find_anagrams("diaper", candidates) == expected

    def test_detects_two_anagrams(self) -> None:
        candidates = ["stream", "pigeon", "maters"]
        expected = ["stream", "maters"]
        assert find_anagrams("master", candidates) == expected

    def test_does_not_detect_anagram_subsets(self) -> None:
        candidates = ["dog", "goody"]
        expected: list[str] = []
        assert find_anagrams("good", candidates) == expected

    def test_detects_anagram(self) -> None:
        candidates = ["enlists", "google", "inlets", "banana"]
        expected = ["inlets"]
        assert find_anagrams("listen", candidates) == expected

    def test_detects_three_anagrams(self) -> None:
        candidates = ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]
        expected = ["gallery", "regally", "largely"]
        assert find_anagrams("allergy", candidates) == expected

    def test_detects_multiple_anagrams_with_different_case(self) -> None:
        candidates = ["Eons", "ONES"]
        expected = ["Eons", "ONES"]
        assert find_anagrams("nose", candidates) == expected

    def test_does_not_detect_non_anagrams_with_identical_checksum(self) -> None:
        candidates = ["last"]
        expected: list[str] = []
        assert find_anagrams("mass", candidates) == expected

    def test_detects_anagrams_case_insensitively(self) -> None:
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        assert find_anagrams("Orchestra", candidates) == expected

    def test_detects_anagrams_using_case_insensitive_subject(self) -> None:
        candidates = ["cashregister", "carthorse", "radishes"]
        expected = ["carthorse"]
        assert find_anagrams("Orchestra", candidates) == expected

    def test_detects_anagrams_using_case_insensitive_possible_matches(self) -> None:
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        assert find_anagrams("orchestra", candidates) == expected

    def test_does_not_detect_an_anagram_if_the_original_word_is_repeated(self) -> None:
        candidates = ["go Go GO"]
        expected: list[str] = []
        assert find_anagrams("go", candidates) == expected

    def test_anagrams_must_use_all_letters_exactly_once(self) -> None:
        candidates = ["patter"]
        expected: list[str] = []
        assert find_anagrams("tapper", candidates) == expected

    def test_words_are_not_anagrams_of_themselves_case_insensitive(self) -> None:
        candidates = ["BANANA", "Banana", "banana"]
        expected: list[str] = []
        assert find_anagrams("BANANA", candidates) == expected

    def test_words_other_than_themselves_can_be_anagrams(self) -> None:
        candidates = ["Listen", "Silent", "LISTEN"]
        expected = ["Silent"]
        assert find_anagrams("LISTEN", candidates) == expected
