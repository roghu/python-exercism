from src.pig_latin import translate


class TestPigLatin:
    def test_word_beginning_with_a(self) -> None:
        assert translate("apple") == "appleay"

    def test_word_beginning_with_e(self) -> None:
        assert translate("ear") == "earay"

    def test_word_beginning_with_i(self) -> None:
        assert translate("igloo") == "iglooay"

    def test_word_beginning_with_o(self) -> None:
        assert translate("object") == "objectay"

    def test_word_beginning_with_u(self) -> None:
        assert translate("under") == "underay"

    def test_word_beginning_with_a_vowel_and_followed_by_a_qu(self) -> None:
        assert translate("equal") == "equalay"

    def test_word_beginning_with_p(self) -> None:
        assert translate("pig") == "igpay"

    def test_word_beginning_with_k(self) -> None:
        assert translate("koala") == "oalakay"

    def test_word_beginning_with_x(self) -> None:
        assert translate("xenon") == "enonxay"

    def test_word_beginning_with_q_without_a_following_u(self) -> None:
        assert translate("qat") == "atqay"

    def test_word_beginning_with_ch(self) -> None:
        assert translate("chair") == "airchay"

    def test_word_beginning_with_qu(self) -> None:
        assert translate("queen") == "eenquay"

    def test_word_beginning_with_qu_and_a_preceding_consonant(self) -> None:
        assert translate("square") == "aresquay"

    def test_word_beginning_with_th(self) -> None:
        assert translate("therapy") == "erapythay"

    def test_word_beginning_with_thr(self) -> None:
        assert translate("thrush") == "ushthray"

    def test_word_beginning_with_sch(self) -> None:
        assert translate("school") == "oolschay"

    def test_word_beginning_with_yt(self) -> None:
        assert translate("yttria") == "yttriaay"

    def test_word_beginning_with_xr(self) -> None:
        assert translate("xray") == "xrayay"

    def test_y_is_treated_like_a_consonant_at_the_beginning_of_a_word(self) -> None:
        assert translate("yellow") == "ellowyay"

    def test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster(self) -> None:
        assert translate("rhythm") == "ythmrhay"

    def test_y_as_second_letter_in_two_letter_word(self) -> None:
        assert translate("my") == "ymay"

    def test_a_whole_phrase(self) -> None:
        assert translate("quick fast run") == "ickquay astfay unray"
