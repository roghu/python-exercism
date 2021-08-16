from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Robot:
    def __init__(
        self, direction: Direction = Direction.NORTH, x: int = 0, y: int = 0
    ) -> None:
        self.direction = direction
        self._x = x
        self._y = y

    @property
    def coordinates(self) -> tuple[int, int]:
        return (self._x, self._y)

    def move(self, instructions: str) -> None:
        for instruction in instructions:
            if instruction == "R":
                self._move_right()
            elif instruction == "L":
                self._move_left()
            elif instruction == "A":
                self._advance_forward()

    def _move_right(self) -> None:
        if self.direction == Direction.NORTH:
            self.direction = Direction.EAST
        elif self.direction == Direction.EAST:
            self.direction = Direction.SOUTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.WEST:
            self.direction = Direction.NORTH

    def _move_left(self) -> None:
        if self.direction == Direction.NORTH:
            self.direction = Direction.WEST
        elif self.direction == Direction.EAST:
            self.direction = Direction.NORTH
        elif self.direction == Direction.SOUTH:
            self.direction = Direction.EAST
        elif self.direction == Direction.WEST:
            self.direction = Direction.SOUTH

    def _advance_forward(self) -> None:
        if self.direction == Direction.NORTH:
            self._y += 1
        elif self.direction == Direction.SOUTH:
            self._y -= 1
        elif self.direction == Direction.EAST:
            self._x += 1
        elif self.direction == Direction.WEST:
            self._x -= 1
