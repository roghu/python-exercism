from src.two_fer import two_fer


class TestTwoFer:
    def test_no_name_given(self) -> None:
        assert two_fer() == "One for you, one for me."

    def test_a_name_given(self) -> None:
        assert two_fer("Alice") == "One for Alice, one for me."

    def test_another_name_given(self) -> None:
        assert two_fer("Bob") == "One for Bob, one for me."
