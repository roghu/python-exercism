PLANTS = {"R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets"}

default_students = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Lleana",
    "Joseph",
    "Kincaid",
    "Larry",
]


class Garden:
    def __init__(self, diagram: str, students: list[str] = default_students) -> None:
        if students != default_students:
            students = sorted(students)
        self._db = self._format(diagram, students)

    def plants(self, name: str) -> list[str]:
        return self._db[name]

    def _format(self, diagram: str, students: list[str]) -> dict[str, list[str]]:
        result = {}
        rows = [row for row in diagram.split("\n")]
        num_of_students = len(rows[0]) // 2

        for i, student in enumerate(students[:num_of_students]):
            x = i * 2
            y = x + 1
            plants = []
            for row in rows:
                plants.append(PLANTS[row[x]])
                plants.append(PLANTS[row[y]])

            result[student] = plants
        return result
