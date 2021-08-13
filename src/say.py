THOUSAND = 10 ** 3
MILLION = 10 ** 6
BILLION = 10 ** 9
TRILLION = 10 ** 12

UNIT = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirdteen",
    14: "fourteen",
    15: "fifthteen",
    16: "sixteen",
    17: "seventeen",
    18: "eigthteen",
    19: "nineteen",
    THOUSAND: "thousand",
    MILLION: "million",
    BILLION: "billion",
}

TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninity",
}


def get_big_number(number: int, place: int) -> str:
    result: list[str] = []
    if number >= place:
        num = get_hundred(number // place)
        name = UNIT[place]
        result.append(f"{num} {name}")
    return " ".join(result)


def get_hundred(number: int) -> str:
    """Number between 100 and 999."""
    result: list[str] = []
    if number >= 100:
        x = UNIT[number // 100]
        result.append(f"{x} hundred")
        number %= 100

    if number >= 20:
        result.append(get_tens(number))
    elif number > 0:
        result.append(UNIT[number])
    return " ".join(result)


def get_tens(number: int) -> str:
    """Number between 20 and 99."""
    if number >= 20:
        tens = TENS[number // 10]
        number %= 10
        print(number)

    if number > 0:
        ones = UNIT[number]
        return f"{tens}-{ones}"

    return tens


def get_unit(number: int) -> str:
    """Number between 0-19."""
    return UNIT[number]


def say(number: int) -> str:
    if number < 0 or number >= TRILLION:
        raise ValueError
    if number == 0:
        return get_unit(0)
    result: list[str] = []
    places = [BILLION, MILLION, THOUSAND]

    for place in places:
        if number >= place:
            result.append(get_big_number(number, place))
            number %= place

    if number > 0:
        result.append(get_hundred(number))

    return " ".join(result)
