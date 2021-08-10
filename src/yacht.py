from collections import Counter
from enum import Enum, auto


class Category(Enum):
    YACHT = auto()
    ONES = auto()
    TWOS = auto()
    THREES = auto()
    FOURS = auto()
    FIVES = auto()
    SIXES = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    LITTLE_STRAIGHT = auto()
    BIG_STRAIGHT = auto()
    CHOICE = auto()


def score(dice: list[int], category: Category) -> int:
    dice = sorted(dice)
    dice_dict = dict(Counter(dice))

    if category == Category.ONES:
        if 1 in dice_dict:
            return dice_dict[1]
    elif category == Category.TWOS:
        if 2 in dice_dict:
            return dice_dict[2] * 2
    elif category == Category.THREES:
        if 3 in dice_dict:
            return dice_dict[3] * 3
    elif category == Category.FOURS:
        if 4 in dice_dict:
            return dice_dict[4] * 4
    elif category == Category.FIVES:
        if 5 in dice_dict:
            return dice_dict[5] * 5
    elif category == Category.SIXES:
        if 6 in dice_dict:
            return dice_dict[6] * 6
    elif category == Category.FOUR_OF_A_KIND:
        for num, count in dice_dict.items():
            if count >= 4:
                return num * 4
    elif category == Category.FULL_HOUSE:
        if sorted(list(dice_dict.values())) == [2, 3]:
            return sum(num * count for num, count in dice_dict.items())
    elif category == Category.LITTLE_STRAIGHT:
        if dice == [1, 2, 3, 4, 5]:
            return 30
    elif category == Category.BIG_STRAIGHT:
        if dice == [2, 3, 4, 5, 6]:
            return 30
    elif category == Category.YACHT:
        for count in dice_dict.values():
            if count == 5:
                return 50
    elif category == Category.CHOICE:
        return sum(dice)
    return 0
