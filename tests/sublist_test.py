from src.sublist import Category, sublist


class TestSublist:
    def test_empty_lists(self) -> None:
        assert sublist([], []) == Category.EQUAL

    def test_empty_list_within_non_empty_list(self) -> None:
        assert sublist([], [1, 2, 3]) == Category.SUBLIST

    def test_non_empty_list_contains_empty_list(self) -> None:
        assert sublist([1, 2, 3], []) == Category.SUPERLIST

    def test_list_equals_itself(self) -> None:
        assert sublist([1, 2, 3], [1, 2, 3]) == Category.EQUAL

    def test_different_lists(self) -> None:
        assert sublist([1, 2, 3], [2, 3, 4]) == Category.UNEQUAL

    def test_false_start(self) -> None:
        assert sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]) == Category.SUBLIST

    def test_consecutive(self) -> None:
        assert sublist([1, 1, 2], [0, 1, 1, 1, 2, 1, 2]) == Category.SUBLIST

    def test_sublist_at_start(self) -> None:
        assert sublist([0, 1, 2], [0, 1, 2, 3, 4, 5]) == Category.SUBLIST

    def test_sublist_in_middle(self) -> None:
        assert sublist([2, 3, 4], [0, 1, 2, 3, 4, 5]) == Category.SUBLIST

    def test_sublist_at_end(self) -> None:
        assert sublist([3, 4, 5], [0, 1, 2, 3, 4, 5]) == Category.SUBLIST

    def test_at_start_of_superlist(self) -> None:
        assert sublist([0, 1, 2, 3, 4, 5], [0, 1, 2]) == Category.SUPERLIST

    def test_in_middle_of_superlist(self) -> None:
        assert sublist([0, 1, 2, 3, 4, 5], [2, 3]) == Category.SUPERLIST

    def test_at_end_of_superlist(self) -> None:
        assert sublist([0, 1, 2, 3, 4, 5], [3, 4, 5]) == Category.SUPERLIST

    def test_first_list_missing_element_from_second_list(self) -> None:
        assert sublist([1, 3], [1, 2, 3]) == Category.UNEQUAL

    def test_second_list_missing_element_from_first_list(self) -> None:
        assert sublist([1, 2, 3], [1, 3]) == Category.UNEQUAL

    def test_order_matters_to_a_list(self) -> None:
        assert sublist([1, 2, 3], [3, 2, 1]) == Category.UNEQUAL

    def test_same_digits_but_different_numbers(self) -> None:
        assert sublist([1, 0, 1], [10, 1]) == Category.UNEQUAL

    def test_unique_return_values(self) -> None:
        assert (
            len(
                set(
                    [
                        Category.SUBLIST,
                        Category.SUPERLIST,
                        Category.EQUAL,
                        Category.UNEQUAL,
                    ]
                )
            )
            == 4
        )

    def test_inner_spaces(self) -> None:
        assert sublist(["a c"], ["a", "c"]) == Category.UNEQUAL

    def test_large_lists(self) -> None:
        assert (
            sublist(
                list(range(1000)) * 1000 + list(range(1000, 1100)),
                list(range(900, 1050)),
            )
            == Category.SUPERLIST
        )

    def test_spread_sublist(self) -> None:
        assert (
            sublist(list(range(3, 200, 3)), list(range(15, 200, 15)))
            == Category.UNEQUAL
        )
