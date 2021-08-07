import json
from typing import Optional, TypedDict, Union

JSON = Union[str, bytes]


class JSON_user(TypedDict):
    name: str
    owes: dict[str, float]
    owed_by: dict[str, float]
    balance: Optional[float]


class UserNotFoundException(BaseException):
    """User Not Found"""


class User:
    def __init__(self, user_item: JSON_user) -> None:
        self.name = user_item["name"]
        self.owes = user_item["owes"]
        self.owed_by = user_item["owed_by"]
        self.balance = 0.0

    def dict(self) -> JSON_user:
        return {
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance,
        }

    def _update_balance(self) -> None:
        self.balance = sum(-i for i in self.owes.values()) + sum(
            i for i in self.owed_by.values()
        )

    def loan_out(self, borrower: str, amount: float) -> None:
        if borrower in self.owes:
            if self.owes[borrower] == amount:
                del self.owes[borrower]
            elif self.owes[borrower] > amount:
                self.owes[borrower] -= amount
            else:
                self.owed_by[borrower] = amount - self.owes[borrower]
                del self.owes[borrower]
        else:
            self.owed_by[borrower] = amount
        self._update_balance()

    def borrows(self, lender: str, amount: float) -> None:
        if lender in self.owed_by:
            if self.owed_by[lender] == amount:
                del self.owed_by[lender]
            elif self.owed_by[lender] > amount:
                self.owed_by[lender] -= amount
            else:
                self.owes[lender] = amount - self.owed_by[lender]
                del self.owed_by[lender]
        else:
            self.owes[lender] = amount
        self._update_balance()


class Database:
    def __init__(self, database: dict[str, list[JSON_user]]) -> None:
        self._db: list[User] = []
        if database:
            for name in database["users"]:
                self._db.append(User(name))

    def add_user(self, user: User) -> None:
        self._db.append(user)

    def get_user(self, name: str) -> tuple[int, User]:
        for i, user in enumerate(self._db):
            if user.name == name:
                return i, user
        raise UserNotFoundException

    def loan(self, lender: str, borrower: str, amount: float) -> None:
        lender_idx, lender_user = self.get_user(lender)
        borrower_idx, borrower_user = self.get_user(borrower)
        lender_user.loan_out(borrower, amount)
        borrower_user.borrows(lender, amount)

        print(self._db[lender_idx].dict())

    def to_JSON(self, names: Optional[list[str]] = None) -> JSON:
        users = []
        if names:
            for user in self._db:
                if user.name in names:
                    users.append(user.dict())
        else:
            users = []
        result = {"users": users}
        return json.dumps(result)


class RestAPI:
    def __init__(self, database: dict[str, list[JSON_user]] = None) -> None:
        if not database:
            database = {"users": []}
        self._db = Database(database)

    def get(self, url: str, payload: Optional[JSON] = None) -> JSON:
        input_ = {}
        if payload:
            input_ = json.loads(payload)
        if url == "/users" and input_:
            return self._db.to_JSON(input_["users"])
        elif url == "/users":
            return self._db.to_JSON()
        return json.dumps("")

    def post(self, url: str, payload: Optional[JSON] = None) -> JSON:
        input_ = {}
        if payload:
            input_ = json.loads(payload)
        if url == "/add" and input_:
            user = User(
                {"name": input_["user"], "owed_by": {}, "owes": {}, "balance": 0.0}
            )
            return json.dumps(user.dict())
        elif url == "/iou" and input_:
            lender = input_["lender"]
            borrower = input_["borrower"]
            amount = input_["amount"]
            self._db.loan(lender, borrower, amount)
            return self._db.to_JSON([lender, borrower])
        return json.dumps("")
