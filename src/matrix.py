class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self._matrix: list[list[int]] = []
        for row_str in matrix_string.split("\n"):
            row = [int(s) for s in row_str.split(" ")]
            self._matrix.append(row)

    def row(self, index: int) -> list[int]:
        return self._matrix[index - 1]

    def column(self, index: int) -> list[int]:
        return [row[index - 1] for row in self._matrix]
