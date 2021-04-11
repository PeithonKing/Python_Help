def first_day(year):
    i = 1
    y = 1
    import LeapYear
    while y < year:
        if LeapYear.leap_year(year): i += 2
        else: i += 1
        y+=1
    return i%7
print(first_day(2020))
