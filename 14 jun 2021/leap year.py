# write a program to find all the leap years between 1900 to 2020
# it should be divisible by 4
# 100 is not a leep year
# the year 400 is a leep year

for year in range(1900,2020):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, end=', ')
