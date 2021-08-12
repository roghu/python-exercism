ITEMS: dict[str, int] = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}


class Allergies:
    def __init__(self, score: int) -> None:
        self._score = score

    def allergic_to(self, item: str) -> bool:
        return bool(ITEMS[item] & self._score)

    @property
    def lst(self) -> list[str]:
        return [item for item in ITEMS.keys() if self.allergic_to(item)]
