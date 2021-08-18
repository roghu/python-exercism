from src.flatten_array import flatten


class TestFlattenArray:
    def test_no_nesting(self) -> None:
        inputs = [0, 1, 2]
        expected = [0, 1, 2]
        assert flatten(inputs) == expected

    def test_flattens_array_with_just_integers_present(self) -> None:
        inputs = [1, [2, 3, 4, 5, 6, 7], 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        assert flatten(inputs) == expected

    def test_5_level_nesting(self) -> None:
        inputs = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
        expected = [0, 2, 2, 3, 8, 100, 4, 50, -2]
        assert flatten(inputs) == expected

    def test_6_level_nesting(self) -> None:
        inputs = [1, [2, [[3]], [4, [[5]]], 6, 7], 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        assert flatten(inputs) == expected

    def test_6_level_nest_list_with_null_values(self) -> None:
        inputs = [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
        expected = [0, 2, 2, 3, 8, 100, -2]
        assert flatten(inputs) == expected

    def test_all_values_in_nested_list_are_null(self) -> None:
        inputs = [None, [[[None]]], None, None, [[None, None], None], None]
        expected: list[int] = []
        assert flatten(inputs) == expected
