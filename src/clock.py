class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        self.hour, self.minute = self._normalize(hour, minute)

    def __repr__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> 'Clock':
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int) -> 'Clock':
        return Clock(self.hour, self.minute - minutes)

    def _normalize(self, hour: int, minute: int) -> tuple[int, int]:
        hour += minute // 60
        minute %= 60
        hour %= 24
        return hour, minute
