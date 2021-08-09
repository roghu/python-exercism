from src.bob import response


class TestBob:
    def test_stating_something(self) -> None:
        assert response("Tom-ay-to, tom-aaaah-to.") == "Whatever."

    def test_shouting(self) -> None:
        assert response("WATCH OUT!") == "Whoa, chill out!"

    def test_shouting_gibberish(self) -> None:
        assert response("FCECDFCAAB") == "Whoa, chill out!"

    def test_asking_a_question(self) -> None:
        assert response("Does this cryogenic chamber make me look fat?") == "Sure."

    def test_asking_a_numeric_question(self) -> None:
        assert response("You are, what, like 15?") == "Sure."

    def test_asking_gibberish(self) -> None:
        assert response("fffbbcbeab?") == "Sure."

    def test_talking_forcefully(self) -> None:
        assert response("Hi there!") == "Whatever."

    def test_using_acronyms_in_regular_speech(self) -> None:
        assert response("It's OK if you don't want to go work for NASA.") == "Whatever."

    def test_forceful_question(self) -> None:
        assert response("WHAT'S GOING ON?") == "Calm down, I know what I'm doing!"

    def test_shouting_numbers(self) -> None:
        assert response("1, 2, 3 GO!") == "Whoa, chill out!"

    def test_no_letters(self) -> None:
        assert response("1, 2, 3") == "Whatever."

    def test_question_with_no_letters(self) -> None:
        assert response("4?") == "Sure."

    def test_shouting_with_special_characters(self) -> None:
        assert (
            response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!")
            == "Whoa, chill out!"
        )

    def test_shouting_with_no_exclamation_mark(self) -> None:
        assert response("I HATE THE DENTIST") == "Whoa, chill out!"

    def test_statement_containing_question_mark(self) -> None:
        assert response("Ending with ? means a question.") == "Whatever."

    def test_non_letters_with_question(self) -> None:
        assert response(":) ?") == "Sure."

    def test_prattling_on(self) -> None:
        assert response("Wait! Hang on. Are you going to be OK?") == "Sure."

    def test_silence(self) -> None:
        assert response("") == "Fine. Be that way!"

    def test_prolonged_silence(self) -> None:
        assert response("          ") == "Fine. Be that way!"

    def test_alternate_silence(self) -> None:
        assert response("\t\t\t\t\t\t\t\t\t\t") == "Fine. Be that way!"

    def test_multiple_line_question(self) -> None:
        assert (
            response("\nDoes this cryogenic chamber make me look fat?\nNo.")
            == "Whatever."
        )

    def test_starting_with_whitespace(self) -> None:
        assert response("         hmmmmmmm...") == "Whatever."

    def test_ending_with_whitespace(self) -> None:
        assert response("Okay if like my  spacebar  quite a bit?   ") == "Sure."

    def test_other_whitespace(self) -> None:
        assert response("\n\r \t") == "Fine. Be that way!"

    def test_non_question_ending_with_whitespace(self) -> None:
        assert (
            response("This is a statement ending with whitespace      ") == "Whatever."
        )
