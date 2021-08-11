def is_armstrong_number(number: int) -> bool:
    lst_nums = list(str(number))
    len_lst = len(lst_nums)
    return sum(int(x) ** len_lst for x in lst_nums) == number
