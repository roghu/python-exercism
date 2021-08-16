from src.robot_simulator import Direction, Robot


class TestRobotCreation:
    def test_at_origin_facing_north(self) -> None:
        robot = Robot(Direction.NORTH, 0, 0)

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.NORTH

    def test_at_negative_position_facing_south(self) -> None:
        robot = Robot(Direction.SOUTH, -1, -1)

        assert robot.coordinates == (-1, -1)
        assert robot.direction == Direction.SOUTH


class TestRobotRotation:
    def test_changes_north_to_east(self) -> None:
        robot = Robot(Direction.NORTH, 0, 0)
        robot.move("R")

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.EAST

    def test_changes_east_to_south(self) -> None:
        robot = Robot(Direction.EAST, 0, 0)
        robot.move("R")

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.SOUTH

    def test_changes_south_to_west(self) -> None:
        robot = Robot(Direction.SOUTH, 0, 0)
        robot.move("R")

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.WEST

    def test_changes_west_to_north(self) -> None:
        robot = Robot(Direction.WEST, 0, 0)
        robot.move("R")

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.NORTH


class TestRotateCounterClockwise:
    def test_changes_north_to_west(self) -> None:
        robot = Robot(Direction.NORTH, 0, 0)
        robot.move("L")

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.WEST

    def test_changes_west_to_south(self) -> None:
        robot = Robot(Direction.WEST, 0, 0)
        robot.move("L")

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.SOUTH

    def test_changes_south_to_east(self) -> None:
        robot = Robot(Direction.SOUTH, 0, 0)
        robot.move("L")

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.EAST

    def test_changes_east_to_north(self) -> None:
        robot = Robot(Direction.EAST, 0, 0)
        robot.move("L")

        assert robot.coordinates == (0, 0)
        assert robot.direction == Direction.NORTH


class TestMovingForwardOne:
    def test_facing_north_increments_y(self) -> None:
        robot = Robot(Direction.NORTH, 0, 0)
        robot.move("A")

        assert robot.coordinates == (0, 1)
        assert robot.direction == Direction.NORTH

    def test_facing_south_decrements_y(self) -> None:
        robot = Robot(Direction.SOUTH, 0, 0)
        robot.move("A")

        assert robot.coordinates == (0, -1)
        assert robot.direction == Direction.SOUTH

    def test_facing_east_increments_x(self) -> None:
        robot = Robot(Direction.EAST, 0, 0)
        robot.move("A")

        assert robot.coordinates == (1, 0)
        assert robot.direction == Direction.EAST

    def test_facing_west_decrements_x(self) -> None:
        robot = Robot(Direction.WEST, 0, 0)
        robot.move("A")

        assert robot.coordinates == (-1, 0)
        assert robot.direction == Direction.WEST


class TestSeriesOfInstructions:
    def test_moving_east_and_north_from_readme(self) -> None:
        robot = Robot(Direction.NORTH, 7, 3)
        robot.move("RAALAL")

        assert robot.coordinates == (9, 4)
        assert robot.direction == Direction.WEST

    def test_moving_west_and_north(self) -> None:
        robot = Robot(Direction.NORTH, 0, 0)
        robot.move("LAAARALA")

        assert robot.coordinates == (-4, 1)
        assert robot.direction == Direction.WEST

    def test_moving_west_and_south(self) -> None:
        robot = Robot(Direction.EAST, 2, -7)
        robot.move("RRAAAAALA")

        assert robot.coordinates == (-3, -8)
        assert robot.direction == Direction.SOUTH

    def test_moving_east_and_north(self) -> None:
        robot = Robot(Direction.SOUTH, 8, 4)
        robot.move("LAAARRRALLLL")

        assert robot.coordinates == (11, 5)
        assert robot.direction == Direction.NORTH
