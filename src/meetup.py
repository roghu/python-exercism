from datetime import date

DAYS_IN_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


class MeetupDayException(BaseException):
    pass


def find_teenth(year: int, month: int, day_of_week: str) -> date:
    teenth = [13, 14, 15, 16, 17, 18, 19]
    for day in teenth:
        date_ = date(year, month, day)
        if date_.strftime("%A") == day_of_week:
            break
    return date_


def find_week(year: int, month: int, week: int, day_of_week: str) -> date:
    count = 0
    if year % 4 == 0:
        days_in_month = 29
    else:
        days_in_month = DAYS_IN_MONTH[month]

    for day in range(1, days_in_month + 1):
        date_ = date(year, month, day)
        if date_.strftime("%A") == day_of_week:
            count += 1
            if count == week:
                return date_
    raise MeetupDayException


def find_last(year: int, month: int, day_of_week: str) -> date:
    try:
        date_ = find_week(year, month, 5, day_of_week)
    except MeetupDayException:
        date_ = find_week(year, month, 4, day_of_week)
    return date_


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    if week == "teenth":
        return find_teenth(year, month, day_of_week)
    elif week == "last":
        return find_last(year, month, day_of_week)

    ordinal = {"1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "5th": 5}
    return find_week(year, month, ordinal[week], day_of_week)
