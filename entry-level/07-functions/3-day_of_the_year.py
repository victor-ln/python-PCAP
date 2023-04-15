#!/usr/bin/env python3

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if (month in [4, 6, 9, 11]):
        return 30
    elif (month == 2):
        if (is_year_leap(year)):
            return 29
        return 28
    else:
        return 31

def day_of_year(year, month, day):
    d = 0

    if not all(isinstance(x, int) for x in (year, month, day)):
        return None

    for m in range(month - 1):
        d += days_in_month(year, m + 1)
    return d + day

print(day_of_year(2000, 12, 31))
