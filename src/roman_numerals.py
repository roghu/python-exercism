UNITS = {9: "IX", 5: "V", 4: "IV", 1: "I"}
TENS = {9: "XC", 5: "L", 4: "XL", 1: "X"}
HUNDRENS = {9: "CM", 5: "D", 4: "CD", 1: "C"}


def _thousand(number: int) -> str:
    return "M" * (number // 1000)


def _small(number: int, place: int, roman: dict[int, str]) -> str:
    if number < place:
        return ""

    number //= place
    if number == 9:
        return roman[9]
    if number == 4:
        return roman[4]

    result = ""
    if number >= 5:
        result = roman[5]
        number %= 5
    return result + (roman[1] * number)


def roman(number: int) -> str:
    result: list[str] = []
    if number >= 1000:
        result.append(_thousand(number))
        number %= 1000

    if number < 1000:
        result.append(_small(number, 100, HUNDRENS))
        number %= 100

    if number < 100:
        result.append(_small(number, 10, TENS))
        number %= 10

    if number < 10:
        result.append(_small(number, 1, UNITS))
    return "".join(result)
