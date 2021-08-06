import re
from typing import Optional

delimiters = re.compile(r"[\s]")


class Luhn:
    def __init__(self, card_num: str) -> None:
        self._card_num: str = re.sub(delimiters, "", card_num)
        self.result: Optional[bool] = None

        if not self._card_num.isdigit():
            self.result = False

    def valid(self) -> bool:
        if self.result is None:
            self.result = self._luhn()
        return self.result

    def _luhn(self) -> bool:
        if len(self._card_num) < 2:
            return False
        nums: list[int] = [int(x) for x in self._card_num]
        for i in range(len(nums) - 2, -1, -2):
            num = nums[i] * 2
            if num > 9:
                num -= 9
            nums[i] = num
        return sum(nums) % 10 == 0
