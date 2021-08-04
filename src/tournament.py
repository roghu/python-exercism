# Can delete after Python 3.10>
# For use of `Team.__lt__` argument type
from __future__ import annotations


class Team:
    def __init__(self, name: str) -> None:
        self.name = name
        self.wins = 0
        self.draws = 0
        self.loses = 0

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Team: {self.name}>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Team):
            return NotImplemented
        return self.points == other.points and self.name == other.name

    def __lt__(self, other: "Team") -> bool:
        if self.points == other.points:
            return self.name > other.name
        return self.points < other.points

    @property
    def points(self) -> int:
        return (self.wins * 3) + (self.draws * 1)

    @property
    def played(self) -> int:
        return self.wins + self.draws + self.loses

    def won(self) -> None:
        self.wins += 1

    def draw(self) -> None:
        self.draws += 1

    def lose(self) -> None:
        self.loses += 1


def get_result(
    result_db: dict[str, Team], home: str, away: str, result: str
) -> dict[str, Team]:
    # Make sure teams are in database
    if home not in result_db:
        result_db[home] = Team(home)
    if away not in result_db:
        result_db[away] = Team(away)

    # See who won
    if result == "win":
        result_db[home].won()
        result_db[away].lose()
    elif result == "loss":
        result_db[home].lose()
        result_db[away].won()
    elif result == "draw":
        result_db[home].draw()
        result_db[away].draw()

    return result_db


class Table:
    def __init__(self, db: list[Team]) -> None:
        self.db = db

    def line_template(
        self, name: str, games_played: str, wins: str, draw: str, lose: str, points: str
    ) -> str:
        return (
            f"{name:<31}|{games_played:>3} |{wins:>3} |"
            f"{draw:>3} |{lose:>3} |{points:>3}"
        )

    def header(self) -> str:
        return self.line_template("Team", "MP", "W", "D", "L", "P")

    def build(self) -> list[str]:
        table: list[str] = []
        table.append(self.header())
        for team in self.db:
            table.append(
                self.line_template(
                    team.name,
                    str(team.played),
                    str(team.wins),
                    str(team.draws),
                    str(team.loses),
                    str(team.points),
                )
            )
        return table


def tally(rows: list[str]) -> list[str]:
    result_db: dict[str, Team] = {}
    for row in rows:
        home, away, result = row.split(";")
        result_db = get_result(result_db, home, away, result)

    table = Table(sorted(result_db.values(), reverse=True))
    return table.build()
