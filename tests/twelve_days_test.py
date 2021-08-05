from src.twelve_days import recite


class TestTwelveDays:
    def test_first_day_a_partridge_in_a_pear_tree(self) -> None:
        expected = [
            "On the first day of Christmas my true love gave to me: "
            "a Partridge in a Pear Tree."
        ]
        assert recite(1, 1) == expected

    def test_second_day_two_turtle_doves(self) -> None:
        expected = [
            "On the second day of Christmas my true love gave to me: "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(2, 2) == expected

    def test_third_day_three_french_hens(self) -> None:
        expected = [
            "On the third day of Christmas my true love gave to me: "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(3, 3) == expected

    def test_fourth_day_four_calling_birds(self) -> None:
        expected = [
            "On the fourth day of Christmas my true love gave to me: "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(4, 4) == expected

    def test_fifth_day_five_gold_rings(self) -> None:
        expected = [
            "On the fifth day of Christmas my true love gave to me: "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(5, 5) == expected

    def test_sixth_day_six_geese_a_laying(self) -> None:
        expected = [
            "On the sixth day of Christmas my true love gave to me: "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(6, 6) == expected

    def test_seventh_day_seven_swans_a_swimming(self) -> None:
        expected = [
            "On the seventh day of Christmas my true love gave to me: "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(7, 7) == expected

    def test_eighth_day_eight_maids_a_milking(self) -> None:
        expected = [
            "On the eighth day of Christmas my true love gave to me: "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(8, 8) == expected

    def test_ninth_day_nine_ladies_dancing(self) -> None:
        expected = [
            "On the ninth day of Christmas my true love gave to me: "
            "nine Ladies Dancing, "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(9, 9) == expected

    def test_tenth_day_ten_lords_a_leaping(self) -> None:
        expected = [
            "On the tenth day of Christmas my true love gave to me: "
            "ten Lords-a-Leaping, "
            "nine Ladies Dancing, "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(10, 10) == expected

    def test_eleventh_day_eleven_pipers_piping(self) -> None:
        expected = [
            "On the eleventh day of Christmas my true love gave to me: "
            "eleven Pipers Piping, "
            "ten Lords-a-Leaping, "
            "nine Ladies Dancing, "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(11, 11) == expected

    def test_twelfth_day_twelve_drummers_drumming(self) -> None:
        expected = [
            "On the twelfth day of Christmas my true love gave to me: "
            "twelve Drummers Drumming, "
            "eleven Pipers Piping, "
            "ten Lords-a-Leaping, "
            "nine Ladies Dancing, "
            "eight Maids-a-Milking, "
            "seven Swans-a-Swimming, "
            "six Geese-a-Laying, "
            "five Gold Rings, "
            "four Calling Birds, "
            "three French Hens, "
            "two Turtle Doves, "
            "and a Partridge in a Pear Tree."
        ]
        assert recite(12, 12) == expected

    def test_recites_first_three_verses_of_the_song(self) -> None:
        expected = [recite(n, n)[0] for n in range(1, 4)]
        assert recite(1, 3) == expected

    def test_recites_three_verses_from_the_middle_of_the_song(self) -> None:
        expected = [recite(n, n)[0] for n in range(4, 7)]
        assert recite(4, 6) == expected

    def test_recites_the_whole_song(self) -> None:
        expected = [recite(n, n)[0] for n in range(1, 13)]
        assert recite(1, 12) == expected
