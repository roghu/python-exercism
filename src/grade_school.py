from collections import defaultdict


class School:
    def __init__(self) -> None:
        self._db: dict[int, list[str]] = defaultdict(list)

    def add_student(self, name: str, grade: int) -> None:
        self._db[grade].append(name)
        self._db[grade] = sorted(self._db[grade])

    def roster(self) -> list[str]:
        result = []
        for _, v in sorted(self._db.items()):
            result.extend(v)
        return result

    def grade(self, grade_number: int) -> list[str]:
        return self._db[grade_number]
