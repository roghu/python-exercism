DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

VERSES = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves,",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,",
]


def verse(day: int) -> str:
    result = [f"On the {DAYS[day]} day of Christmas my true love gave to me:"]
    for i in range(day, -1, -1):
        if day != 0 and i == 0:
            result.append(f"and {VERSES[i]}")
        else:
            result.append(VERSES[i])
    return " ".join(result)


def recite(start_verse: int, end_verse: int) -> list[str]:
    result = []
    for i in range(start_verse - 1, end_verse):
        result.append(verse(i))
    return result
