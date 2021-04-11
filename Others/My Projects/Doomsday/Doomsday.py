days = {"Sunday": 0, "Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
from LeapYear import leap_year
days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

while True:
    year = input("\nEnter the year: ")
    if year == "quit": break
    first_day = (input("Enter the first day of the year: ")).title()
    if leap_year(int(year)):
        days_in_months[2] = 29
    i = days[first_day]
    c = 0
    m = 0
    s = 12+i
    for d in days_in_months:
        s += d
        if s % 7 == days["Friday"]:
            print("13th " + months[m] + " is a Friday!")
            c += 1
        m += 1
    print("There are " + str(c) + " dooms days this year!")
input("\nPress enter to exit")
